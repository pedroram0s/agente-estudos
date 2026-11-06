
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0

import datetime
import os
from pathlib import Path
from typing import Optional

from google.adk.agents import Agent
from google.adk.agents.readonly_context import ReadonlyContext
from google.adk.apps import App
from google.adk.environment import LocalEnvironment
from google.adk.models import Gemini
from google.adk.skills import load_skills_from_dir
from google.adk.tools.base_tool import BaseTool
from google.adk.tools.environment import EnvironmentToolset as _BaseEnvironmentToolset
from google.adk.tools.skill_toolset import SkillToolset
from google.genai import types


# ==================================================
# MODEL CONFIGURATION
# ==================================================

# Uses the MODEL environment variable.
# Falls back to Gemini 3.5 Flash Lite if not configured.

MODEL = os.getenv("MODEL") or "gemini-3.5-flash-lite"


# ==================================================
# ENVIRONMENT TOOLSET
# ==================================================

class EnvironmentToolset(_BaseEnvironmentToolset):
    """EnvironmentToolset that respects tool_filter."""

    async def get_tools(
        self, readonly_context: Optional[ReadonlyContext] = None
    ) -> list[BaseTool]:

        tools = await super().get_tools(readonly_context)

        if self.tool_filter:
            return [
                tool
                for tool in tools
                if self._is_tool_selected(tool, readonly_context)
            ]

        return tools


# ==================================================
# PROJECT PATHS
# ==================================================

BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR.parent

SKILLS_DIR = BASE_DIR / "skills"
PLANOS_DIR = PROJECT_DIR / "planos"


# Ensure the plans directory exists.
PLANOS_DIR.mkdir(parents=True, exist_ok=True)


# ==================================================
# SKILLS CONFIGURATION
# ==================================================

skills = load_skills_from_dir(SKILLS_DIR)

skill_toolset = SkillToolset(
    skills=skills
)


# ==================================================
# LOCAL ENVIRONMENT
# ==================================================

# Local storage for generated study plans.
# This configuration is intended for local development.
# Production storage can be integrated with Google Cloud Storage later.

local_environment = LocalEnvironment(
    working_dir=PLANOS_DIR
)


# ==================================================
# FILE TOOLS
# ==================================================

# Exposes only ReadFile and WriteFile.

env_toolset = EnvironmentToolset(
    environment=local_environment,
    tool_filter=["ReadFile", "WriteFile"],
)


# ==================================================
# AGENT INSTRUCTIONS
# ==================================================

today = datetime.date.today()

today_iso = today.isoformat()
today_br = today.strftime("%d/%m/%Y")


instruction = f"""
Você é o agente-estudos, um mentor de estudos especializado em criar
planos de estudo personalizados.

Suas responsabilidades incluem:

- Criar planos de estudo personalizados.
- Organizar conteúdos por etapas de aprendizagem.
- Aplicar revisões espaçadas.
- Criar checkpoints de autoavaliação.
- Organizar atividades práticas.
- Gerar agendas exportáveis para o Google Agenda em CSV.

Data atual: {today_iso} ({today_br}).

Utilize sempre essa data como referência para planejar os cronogramas
e calcular datas relativas.

Siga rigorosamente as instruções da Skill 'plano-de-estudos'.

Antes de gerar um cronograma, verifique as informações obrigatórias
solicitadas pela Skill.

Carregue e utilize os recursos da Skill conforme necessário.

Ao finalizar um cronograma:

1. Utilize a ferramenta WriteFile para salvar o arquivo.
2. Utilize o caminho 'plano-de-estudos.csv'.
3. Salve o arquivo dentro da pasta de planos configurada no ambiente.
4. Confirme ao usuário que o arquivo foi gerado.

Não invente informações que o usuário não forneceu.
"""


# ==================================================
# ROOT AGENT
# ==================================================

root_agent = Agent(
    name="agente_estudos",
    model=Gemini(
        model=MODEL,
        retry_options=types.HttpRetryOptions(
            attempts=3,
        ),
    ),
    instruction=instruction,
    tools=[
        skill_toolset,
        env_toolset,
    ],
)


# ==================================================
# APPLICATION
# ==================================================

app = App(
    root_agent=root_agent,
    name="app",
)
