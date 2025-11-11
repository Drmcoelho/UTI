# Módulo 02 — Monitorização Hemodinâmica Não Invasiva

> **Objetivo geral:** estruturar um protocolo robusto de monitorização não invasiva em UTI, integrando equipamentos oscilométricos, índice de perfusão e ecocardiografia point-of-care.

## 🔍 Visão geral

- **Carga sugerida:** 3h teóricas + 1h de prática com equipamentos
- **Pré-requisitos:** interpretação básica de ecocardiografia à beira leito, fundamentos de fisiologia cardiovascular
- **Competências-chave:**
  - Validar a confiabilidade de equipamentos oscilométricos
  - Implementar trending de PAM, índice de perfusão e VTI
  - Identificar limites que exigem escalonamento para monitorização invasiva
  - Documentar e comunicar a evolução hemodinâmica com precisão

## 📘 Trilhas teóricas

1. **Tecnologias disponíveis**
   - Algoritmos oscilométricos e limitações mais comuns
   - Monitorização contínua vs intermitente: quando utilizar
   - Índice de perfusão e correlação com débito cardíaco
2. **Integração com ecocardiografia POCUS**
   - Medida do TSV e cálculo do VTI
   - Estimativa do débito cardíaco não invasivo
   - Critérios para repetição e validação das medidas
3. **Tomada de decisão**
   - Limiares para migração ao cateter arterial
   - Comunicação de trending em rounds
   - Checklist de documentação padronizada

> 📄 **Material-base:** execute o notebook [`02_monitorizacao_hemodinamica_nao_invasiva.ipynb`](../notebooks/02_monitorizacao_hemodinamica_nao_invasiva.ipynb) enquanto acompanha este módulo.

## 📝 Prática aplicada

- **Exercícios:** Bloco 2 em [`exercicios/exercicios_blocos_1-3.md`](../exercicios/exercicios_blocos_1-3.md)
- **Caso clínico:** [`casos-clinicos/caso_02_monitorizacao_nao_invasiva.md`](../casos-clinicos/caso_02_monitorizacao_nao_invasiva.md)
- **Simulador:** [`simuladores/modulo_02_monitorizacao_nao_invasiva.py`](../simuladores/modulo_02_monitorizacao_nao_invasiva.py)

## 🧠 Revisão ativa

- **Flashcards:** [`flashcards/02_monitorizacao_hemodinamica_nao_invasiva.txt`](../flashcards/02_monitorizacao_hemodinamica_nao_invasiva.txt)
- **Recursos de bolso:** [`recursos/02_monitorizacao_nao_invasiva/`](../recursos/02_monitorizacao_nao_invasiva/)
- **Script Scriptable:** [`scriptable/modulo_02_monitorizacao_nao_invasiva.js`](../scriptable/modulo_02_monitorizacao_nao_invasiva.js)

## ✅ Critérios de conclusão

- Validar três séries consecutivas de PAM com diferença ≤ 5 mmHg
- Calcular débito cardíaco não invasivo a partir de VTI em dois pacientes
- Documentar trending completo usando a planilha do módulo
- Resolver o caso clínico e gabarito
- Registrar plano de escalonamento caso critérios de alarme sejam atingidos
