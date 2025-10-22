# Curso Codex + Drmcoelho/UTI — do Iniciante ao Mega‑Avançado (Robustíssimo)

> Guia completo e prático para dominar o Codex (Web, CLI e VS Code) trabalhando no repositório **Drmcoelho/UTI**. Inclui trilha de 30 dias, laboratórios, checklists, templates e banco de prompts.

---

## 0) Visão Geral
- **Objetivo**: permitir que você use o Codex como um “par programador” para criar, refatorar, testar, revisar e automatizar tarefas no repositório **UTI** com qualidade e segurança.
- **Público**: de iniciante a mega‑avançado.
- **Formato**: módulos progressivos com labs guiados, rubricas de avaliação e artefatos reutilizáveis.

### Resultados de Aprendizagem
1. Configurar Codex (Web/CLI/VS Code) e conectar ao repo **Drmcoelho/UTI** (branch, permissões, ambiente).  
2. Conduzir edições multi‑arquivo, rodar testes/notebooks e abrir PRs com padrão profissional.  
3. Projetar prompts e fluxos robustos (planejamento, verificação, evidências).  
4. Automatizar tarefas (terminal, scripts, jobs) e revisar código com IA.  
5. Customizar comportamento (AGENTS.md, políticas, checklists, CI) e otimizar performance.

---

## 1) Preparação do Ambiente
### 1.1 Acesso e Autenticação
- Conta ChatGPT/Codex habilitada.  
- GitHub autorizado (escopos mínimos: repo, pull_request).  
- **2FA** ativado.

### 1.2 Clonar e Isolar Ambiente
- `git clone https://github.com/Drmcoelho/UTI.git`
- Python 3.10+ / conda ou venv: `python -m venv .venv && source .venv/bin/activate`
- Dependências: `pip install -r requirements.txt` (ajuste conforme repo).

### 1.3 Ferramentas Codex
- **Web**: painel Codex em ChatGPT (selecionar repo/branch).  
- **CLI**: instalar `codex` (ou wrapper equivalente); autenticar.  
- **VS Code**: extensão OpenAI Codex; login; habilitar *contexto automático*.

### 1.4 Convenções Recomendadas (padrão do curso)
- Branch por tarefa: `feat/*`, `fix/*`, `docs/*`, `refactor/*`.  
- Commits atômicos (Conventional Commits opcional).  
- Docstrings PT‑BR, PEP 8 (linha 100–120 col).  
- Pasta `tests/` e/ou execução de notebooks com `nbmake`/`papermill`.

---

## 2) Tour das Interfaces do Codex
### 2.1 Web (Sandbox de Tarefas)
- Prompt → escolha do repo/branch → execução em sandbox → artefatos (diffs, logs, evidências).  
- Modos: *Ask* (explicar) e *Code* (agir).  

### 2.2 CLI (Automação Local)
- Sessão interativa; comandos naturais + atalhos (`/open`, `/files`, `/run`).  
- Pode instalar deps, rodar testes, editar arquivos, gerar diffs.

### 2.3 VS Code (Contexto do Workspace)
- Chat lateral + sugestões inline.  
- Ações contextuais (“explicar trecho”, “refatorar”, “gerar teste”).

---

## 3) Quickstart (90 minutos)
1. **Selecionar repo** `Drmcoelho/UTI` (branch `main`).  
2. **Lab #QS‑1 — Diagnóstico**: “Liste subpastas e arquivos-chave; resuma objetivos do projeto; identifique notebooks mais usados.”  
3. **Lab #QS‑2 — Função utilitária**: gerar `utils/peso_predito.py` com PBW (docstring + testes).  
4. **Lab #QS‑3 — PR**: criar branch `feat/pbw`, rodar testes/notebooks críticos, abrir PR com descrição template.

---

## 4) Fundamentos (Iniciante)
### 4.1 Prompts Essenciais
- Estrutura **Tarefa → Contexto → Restrições → Saída Esperada**.  
- Ex.: “No arquivo X, *adicione* função Y **sem** quebrar Z; inclua testes unitários; gere diff e explicação.”

### 4.2 Navegação e Leitura do Código
- Pedir resumos por arquivo, busca de símbolos, mapa de dependências.  
- *Pitfall*: peças longas → peça *sumários hierárquicos*.

### 4.3 Edição Segura
- Sempre em branch.  
- Solicitar **diff unificado** + **racional** da mudança.  
- Validar em ambiente local (CLI/VS Code) antes de push.

### 4.4 Labs (Iniciante)
- **Lab I‑1**: explicar notebook *SDRA*; extrair fórmulas.  
- **Lab I‑2**: função `conversao_temp()` + testes.  
- **Lab I‑3**: docstrings padronizadas em um módulo.

---

## 5) Intermediário — Edição Multi‑Arquivo e Execução
### 5.1 Padrões de Prompt Contextual
- *Exemplar + variar*: mostrar um arquivo modelo para replicar estrutura.  
- *Comando de cobertura*: “aplique em todos notebooks que contêm …”.

### 5.2 Testes, Notebooks e Dados
- Rodar `pytest -q`; snapshot tests para gráficos.  
- Executar notebooks com `nbmake`/`papermill`; coletar falhas.

### 5.3 Refatoração Cruzada
- Extrair funções duplicadas para `utils/`.  
- Atualizar imports e notebooks consumidores.  

### 5.4 Labs (Intermediário)
- **Lab M‑1**: criar `simuladores/dose_antibiotico.py` e notebook novo.  
- **Lab M‑2**: refatorar funções repetidas em 2 notebooks.  
- **Lab M‑3**: pipeline para executar todos os notebooks e reportar erros.

---

## 6) Avançado — Automação, Voz e Colaboração
### 6.1 Automação no Terminal
- Sequências: instalar deps → rodar lint/format → testes → gerar relatório markdown.  
- Scripts `tasks/` para o Codex invocar.

### 6.2 Comandos por Voz (opcional)
- Ditado do SO/Whisper → entrada do Codex (CLI/Web).  
- Padrões de fala: instrução única, confirmar, prosseguir.

### 6.3 Fluxo Git Profissional
- Branches temáticos; PRs pequenas; *draft PR*.  
- Mensagens de commit geradas pelo Codex (revise!).  
- Checklist de PR (abaixo).

### 6.4 Revisão Assistida
- Pedir: “revise diff/PR; aponte bugs, *code smells*, sugestões e testes faltantes.”  
- Pedir **evidências** (linhas afetadas, antes/depois, logs).

### 6.5 Labs (Avançado)
- **Lab A‑1**: PR end‑to‑end com revisão do Codex.  
- **Lab A‑2**: automação de execução de notebooks e sumarização das falhas.

---

## 7) Mega‑Avançado — Customização e Performance
### 7.1 AGENTS.md (orientando a IA)
Inclua no topo do repo um `AGENTS.md` com:
- Setup e comandos canônicos (instalar, testar, executar notebooks).  
- Estilo (docstrings PT‑BR; PEP 8; nomes descritivos).  
- Políticas: não alterar dados clínicos; preferir criar módulos a duplicar.  
- Checklists de PR e testes mínimos.  
- “Sempre gerar diff + racional + plano de reversão em caso de falha”.

### 7.2 Integração CI
- GitHub Actions: lint (ruff/flake8), format (black), testes, `nbmake` em matriz.  
- Job opcional: sumarizar falhas com ajuda do Codex e comentar na PR.

### 7.3 Otimização de Performance
- Identificar gargalos (cProfile/line_profiler); pedir otimizações: vetorização NumPy, cache, I/O em lote, paralelismo (joblib).  
- Manter equivalência funcional via testes de regressão.

### 7.4 Auditoria e Segurança
- Escopos limitados; *dry‑run* para operações destrutivas.  
- Evitar segredos/PHI em prompts.  
- Reprodutibilidade: seeds, versões fixadas.

### 7.5 Labs (Mega‑Avançado)
- **Lab X‑1**: criar `AGENTS.md` e validar num ciclo de tarefa.  
- **Lab X‑2**: profile → otimizar função lenta; provar ganho.  
- **Lab X‑3**: pipeline CI com `nbmake` + comentário automático de falhas.

---

## 8) Banco de Prompts (copiar‑colar)
- **Mapa do Projeto**: “Liste diretórios, arquivos críticos e descreva papéis de cada um; gere um diagrama textual de dependências.”
- **Edição Multi‑arquivo**: “Padronize docstrings em PT‑BR em todos os `.py` de `utils/`; gere diff consolidado e resumo.”
- **Teste & Notebook**: “Execute todos os notebooks com `nbmake`; reporte falhas com caminho, célula e stacktrace; proponha correções.”
- **Refatoração**: “Detecte código duplicado envolvendo cálculo de PBW; extraia para `utils/peso_predito.py` com testes.”
- **Revisão de PR**: “Analise este diff; aponte riscos, inconsistências, testes faltantes e oportunidades de simplificação.”
- **Otimização**: “Faça profile desta função; proponha 2 alternativas vetorizadas mantendo saída idêntica; inclua benchmarks.”

---

## 9) Checklists
### 9.1 PR Checklist
- [ ] Branch dedicada criada  
- [ ] Escopo pequeno e claro  
- [ ] Testes atualizados/criados  
- [ ] Notebooks críticos executados  
- [ ] Diff + racional + plano de reversão  
- [ ] CI verde  
- [ ] Revisão do Codex e humana aplicada

### 9.2 Prompt de Alta Qualidade
- [ ] Tarefa clara  
- [ ] Contexto suficiente (arquivos/trechos)  
- [ ] Restrições e padrões  
- [ ] Critérios de aceitação/testes  
- [ ] Solicitar evidências (diff/logs)

---

## 10) Troubleshooting
- **Mudança fora de escopo**: pedir *“reverta e limite a alteração ao arquivo X”*.  
- **Loop de correções**: imponha *orçamento* (passos N) e peça plano antes de executar.  
- **Conflitos Git**: peça *“resolva conflitos mantendo lógica do arquivo A como fonte da verdade; mostre diff final”*.  
- **Notebooks quebrando**: executar célula a célula e capturar primeira falha; pedir correção mínima.

---

## 11) Trilha de 30 Dias (30–60 min/dia)
**Semanas 1–4 (cada dia 1 lab pequeno):**
- **S1 (Fundamentos)**: tour do projeto, prompts básicos, função utilitária, PR simples.  
- **S2 (Intermediário)**: refatoração multi‑arquivo, testes, execução de notebooks, revisão.  
- **S3 (Avançado)**: automação CLI, revisão IA com evidências, fluxo Git sólido.  
- **S4 (Mega)**: AGENTS.md, CI com `nbmake`, profile + otimização, retrospectiva.

> Ao final: abrir uma PR “capstone” que entregue uma melhoria real (nova função, simulador ou refatoração substancial) com testes, docs e performance medida.

---

## 12) Templates
### 12.1 Descrição de PR
**Título**: <tipo>: <escopo curto>

**Resumo**  
- Objetivo da mudança  
- Arquivos impactados  
- Decisões de design

**Testes**  
- Como validar  
- Resultados (logs/prints/notebooks)

**Riscos & Rollback**  
- Riscos potenciais  
- Passos de reversão

### 12.2 Commit (Conventional Commits)
- `feat(utils): adiciona cálculo de PBW com testes`
- `fix(notebooks): corrige import faltante no tema SDRA`
- `refactor(simuladores): extrai lógica de dose para módulo`

---

## 13) Rubricas de Avaliação
- **Correção** (0–5): testes passam, notebooks executam.  
- **Qualidade** (0–5): legibilidade, padrões, docstrings.  
- **Cobertura** (0–5): impacto bem mapeado, sem regressão.  
- **Evidências** (0–5): diffs, logs, benchmarks.  
- **Autonomia Codex** (0–5): uso eficaz de IA com supervisão adequada.

---

## 14) Apêndice — Scripts Úteis (esboços)
- **Executar notebooks**: `pytest --nbmake notebooks/`
- **Benchmark simples**:
```bash
python - <<'PY'
import time, numpy as np
from utils.peso_predito import calcular_peso_predito
h = np.linspace(140, 200, 10)
t0 = time.time();
for _ in range(10000):
    for x in h: calcular_peso_predito(x, 'M')
print('elapsed:', time.time()-t0)
PY
```
- **Pre‑commit (ruff/black)**: adicionar `.pre-commit-config.yaml` e job no CI.

---

## 15) Glossário Essencial
- **AGENTS.md**: guia para orientar agentes de IA no repo.  
- **nbmake**: plugin do pytest para executar notebooks.  
- **Snapshot test**: validação por comparação de saída/figura salva.  
- **Dry‑run**: simulação sem efeito colateral definitivo.

---

### Fim — Próximos Passos
1) Execute os **Labs Quickstart**.  
2) Se ainda não existir, adicione **AGENTS.md** com as convenções acima.  
3) Abra uma PR “capstone” no UTI aplicando o fluxo completo (Codex → testes → PR → revisão).

