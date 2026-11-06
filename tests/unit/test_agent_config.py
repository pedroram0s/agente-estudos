# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import asyncio
import datetime

from app.agent import MODEL, PLANOS_DIR, SKILLS_DIR, root_agent


def test_agent_model_and_instruction() -> None:
    today = datetime.date.today()
    assert isinstance(root_agent.instruction, str)
    assert today.isoformat() in root_agent.instruction
    assert MODEL is not None


def test_paths() -> None:
    assert PLANOS_DIR.name == "planos"
    assert (SKILLS_DIR / "plano-de-estudos" / "SKILL.md").exists()


def test_tools_exposure() -> None:
    tools = asyncio.run(root_agent.canonical_tools())
    tool_names = [t.name for t in tools]

    # Verify only ReadFile and WriteFile are exposed from environment
    assert "ReadFile" in tool_names
    assert "WriteFile" in tool_names
    assert "Execute" not in tool_names
    assert "EditFile" not in tool_names

    # Verify skill tools
    assert "load_skill" in tool_names
    assert "load_skill_resource" in tool_names
