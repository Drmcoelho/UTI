# 🔄 Plano de Revisão Contínua do Conteúdo

Este documento define a cadência de revisão dos materiais do projeto UTI, garantindo atualização contínua com base em
resultados de aprendizagem e novas evidências científicas.

## 📆 Cronograma Oficial

| Mês | Atividade | Responsáveis | Entregáveis |
|-----|-----------|--------------|-------------|
| Janeiro | Revisão rápida de indicadores de aprendizagem do 4º trimestre | Coordenação acadêmica + equipe de dados | Relatório de métricas + lista de ajustes prioritários |
| Abril (1ª semana) | Revisão completa de conteúdo (Q1) | Líderes de módulo | Atualização de notebooks, casos e exercícios + changelog |
| Julho (1ª semana) | Revisão completa de conteúdo (Q2) | Líderes de módulo | Atualização de notebooks, casos e exercícios + changelog |
| Outubro (1ª semana) | Revisão completa de conteúdo (Q3) | Líderes de módulo | Atualização de notebooks, casos e exercícios + changelog |
| Dezembro (2ª semana) | Sprint de consolidação anual | Coordenação acadêmica | Relatório anual de impacto + roadmap do próximo ano |

> **Observação:** Revisões extraordinárias podem ser convocadas se surgirem alertas críticos (p. ex., novas diretrizes de sociedades internacionais).

## 📊 Fontes de Dados para Revisão

1. **Resultados de aprendizagem**: notas de quizzes, desempenho em simuladores, feedback qualitativo de estudantes.
2. **Evidências científicas**: guidelines atualizadas (SCCM, ATS/ERS, Surviving Sepsis), artigos de alto impacto, consensos nacionais.
3. **Avaliação de pares**: revisores externos convidados a cada semestre para auditar coerência científica.
4. **Análise de engajamento**: métricas de acesso aos notebooks, tempo de uso dos simuladores e completion rate dos exercícios.

## ✅ Checklist por Ciclo de Revisão

- [ ] Consolidar métricas de aprendizagem do trimestre
- [ ] Mapear alterações de guidelines relevantes
- [ ] Priorizar módulos críticos (alto volume de uso ou maior índice de erro)
- [ ] Atualizar notebooks, exercícios, casos e simuladores impactados
- [ ] Registrar mudanças no `CHANGELOG` trimestral
- [ ] Comunicar aprendizes sobre novidades e justificativas

## 🧭 Fluxo de Trabalho Recomendado

1. **Preparação (Semana -2)**
   - Extrair dados de quizzes (`exercicios/`), simuladores e notebooks interativos.
   - Coletar feedback qualitativo via formulários.
2. **Revisão Técnica (Semana -1)**
   - Reunir líderes de módulo para revisar evidências novas.
   - Atualizar referências bibliográficas.
3. **Implementação (Semana 0)**
   - Executar atualizações priorizadas.
   - Testar notebooks e simuladores atualizados.
4. **Validação (Semana +1)**
   - Revisão cruzada por outro membro da equipe.
   - Publicação do resumo de mudanças.
5. **Seguimento (Semana +2)**
   - Monitorar dúvidas recorrentes e registrar em backlog.

## 🧩 Integração com Ferramentas do Repositório

- Registrar tarefas de revisão no GitHub Projects ou equivalente com etiquetas `review-qX`.
- Documentar evidências-chave e decisões no diretório `docs/` (subpasta `decisions/` quando criada).
- Atualizar exercícios e simuladores com base nas lacunas identificadas (ver `simuladores/quiz_objetivos_modulos.md`).

## 📣 Comunicação

- Enviar resumo trimestral via newsletter para aprendizes.
- Promover sessão síncrona de 30 minutos após cada revisão trimestral para dúvidas.
- Manter FAQ em `docs/GUIA_DE_USO.md` alinhado com mudanças recentes.

## 🧾 Histórico

| Ano | Ciclo | Principais atualizações | Impacto observado |
|-----|-------|-------------------------|-------------------|
| 2025 | Q1 | Documento inicial de governança publicado | Estabelecimento da cadência trimestral |
| 2025 | Q2 | (preencher após conclusão) |  |

> Atualize esta tabela a cada revisão para manter rastreabilidade institucional.
