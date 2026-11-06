# Fluxo de Trabalho: Montagem do Plano de Estudos

Siga os passos na ordem. Não pule etapas e não mostre os cálculos intermediários para a pessoa, a menos que ela peça. Mostre só o resultado final no formato do template.

---

## Passo 1: Diagnóstico de Capacidade

Com as informações do gating, calcule:

* **Dias de estudo disponíveis**: conte apenas os dias da semana informados, entre a data de início e o **dia anterior** à data-alvo (o dia do objetivo não é dia de estudo).
* **Dias de margem** = 15% dos dias de estudo, arredondado para baixo (mínimo 1). Distribua os dias de margem no **fim das semanas**, começando pela última. Eles não recebem conteúdo novo: servem para recuperar atrasos ou, se tudo estiver em dia, para revisão extra.
* **Horas líquidas** = (dias de estudo − dias de margem) × horas por dia.

Se o prazo tiver menos de 3 dias de estudo, avise que o plano vai ser um **intensivão de revisão** e foque só no essencial.

## Passo 2: Decomposição do Objetivo

1. Quebre o objetivo em **4 a 8 módulos**, ordenados por pré-requisito (o que precisa vir antes).
2. Estime as horas de cada módulo considerando o **nível atual**:
   * Iniciante: estimativa cheia.
   * Intermediário: cerca de 60% da estimativa.
   * Avançado: cerca de 30%, com foco em lacunas e prática.
3. Reserve **20 a 30% das horas líquidas para revisão** (Passo 3) e **10% para a etapa final de simulação** (prova simulada, mock interview ou projeto integrador).
4. **Se a soma não couber nas horas líquidas:** aplique a regra 80/20. Mantenha os módulos que mais pesam no objetivo, marque os demais como `Opcional` e liste-os na seção "O que ficou de fora" do template, explicando por quê.

## Passo 3: Distribuição das Sessões

1. Use `load_skill_resource` para ler `references/tecnicas.md`.
2. Distribua os módulos pelos dias disponíveis, respeitando:
   * **Duração da sessão** igual às horas por dia informadas, dividida em blocos Pomodoro (veja `tecnicas.md`).
   * **Revisão espaçada dinâmica**:
     - O tempo de revisão no início da sessão tem um **teto fixo de 20% do tempo total da sessão** (ex.: até 18 min para sessão de 1h30; até 24 min para 2h).
     - Defina os intervalos com base no horizonte do plano:
       - **Planos curtos (< 14 dias de estudo):** revisões em **D+1 e D+3**.
       - **Planos médios (14 a 45 dias de estudo):** revisões em **D+1, D+3 e D+7**.
       - **Planos longos (> 45 dias de estudo):** revisões em **D+1, D+3, D+7 e D+21**.
     - **Prioridade e resolução de colisões:** **D+1 tem prioridade máxima** (consolidação imediata). Se múltiplas revisões caírem no mesmo dia ou em dia indisponível e atingirem o teto de 20%, mantenha o D+1 no dia e consolide o excedente (D+3/D+7/D+21) no checkpoint semanal mais próximo.
   * **Intercalação**: a partir da segunda semana, misture exercícios de módulos anteriores com o módulo atual.
   * **Técnica e entregável**: cada sessão tem uma técnica principal de `tecnicas.md` e um entregável concreto.
   * **Etapa final**: as últimas sessões antes da data-alvo são de simulação e revisão geral, sem conteúdo novo.
3. Não agende nada nos dias que a pessoa não informou como disponíveis.

## Passo 4: Checkpoints Semanais

No último dia de estudo de cada semana, inclua um **checkpoint** com:

* **3 a 5 perguntas de autoavaliação** (recuperação ativa) sobre o conteúdo da semana e revisões consolidadas pendentes. As perguntas devem ser específicas do assunto, nunca genéricas como "você entendeu o módulo?".
* **1 desafio prático "mão na massa"** sem consulta (ex.: escrever uma função/código, resolver um caso real ou redigir uma solução prática).
* **Critério objetivo de "dominei"**: meta clara de **≥ 80% de acerto** nas perguntas e conclusão com sucesso do desafio prático sem consulta.
* **Ação se não passar (< 80%):** mapear a lacuna específica e direcionar o estudo de recuperação diretamente para o **dia de margem mais próximo** da semana, sem comprometer o avanço do conteúdo novo.

## Passo 5: Montagem da Resposta

1. Use `load_skill_resource` para ler `assets/plano_template.md`.
2. Preencha **todas** as seções do template, na ordem.
3. Monte o **CSV para o Google Agenda** seguindo exatamente as regras descritas no template:
   * Se o plano tiver **até 14 dias de estudo**, inclua todas as sessões.
   * Se tiver **mais de 14**, inclua só os primeiros 14 dias de estudo e avise: "Quer que eu gere o CSV das próximas semanas?".
4. Use `load_skill_resource` para ler `references/salvar_agenda.md` e salve o CSV com a ferramenta `WriteFile` em `plano-de-estudos.csv`, seguindo o checklist e as regras de caminho desse arquivo.
   * Se a ferramenta `WriteFile` não estiver disponível, mostre o CSV num bloco ```` ```csv ```` na seção 5 do template.
5. Na resposta, preencha a seção 5 do template com o **caminho do arquivo salvo** e o número de sessões. Não repita o CSV inteiro na conversa quando o arquivo tiver sido salvo.

## Passo 6: Ajustes e Replanejamento

Depois de entregar o plano, a pessoa pode pedir mudanças. Siga estas regras:

* **"Perdi sessões" / "atrasei"**: não empilhe o conteúdo atrasado em um único dia. Primeiro use os dias de margem; se não bastar, empurre o restante para frente e corte módulos `Opcional`. Nunca corte as revisões D+1.
* **"Mudou minha disponibilidade"**: refaça a partir do Passo 1, mantendo o que já foi estudado.
* **"Quero mais/menos detalhe"**: ajuste só a apresentação, sem refazer o planejamento.
* Em qualquer ajuste, devolva a tabela de sessões atualizada **e** regrave o `plano-de-estudos.csv`, não só a explicação do que mudou. Siga a seção "Replanejamento" de `references/salvar_agenda.md`.
