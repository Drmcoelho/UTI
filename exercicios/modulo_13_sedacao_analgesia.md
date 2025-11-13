# Exercícios — Módulo 13 — Sedação, Analgesia e Conforto

## Como usar

1. Estude o guia [`docs/modulo_13_sedacao_analgesia.md`](../docs/modulo_13_sedacao_analgesia.md) e revise o notebook com fluxos de titulação.
2. Simule cenários com `simuladores/modulo_13_sedacao_analgesia.py` para praticar ajustes de sedativos, analgésicos e monitorização.
3. Execute `python -m exercicios.modulo_13_sedacao_analgesia` para responder às MCQ e V/F com feedback em tempo real.
4. Utilize as questões dissertativas como base para discussão multiprofissional (enfermagem, fisioterapia, farmácia).

---

## Questões dissertativas

1. **Plano multimodal de sedoanalgesia**
   - (a) Como selecionar agentes (opioides, sedativos, adjuvantes) considerando perfis hemodinâmicos?
   - (b) Quais metas RASS e CPOT estabelecer para paciente em ventilação protetora?
   - (c) Como integrar analgesia regional ou técnicas não farmacológicas?
   > 💡 *Gabarito orientador:* Escolha baseada em estabilidade hemodinâmica (dexmedetomidina para preservar respiração, propofol com atenção à pressão, quetamina para analgesia refratária). Definir RASS −2 a 0, CPOT < 3. Integrar bloqueios regionais, fisioterapia, musicoterapia.

2. **Interrupção diária e prevenção de delirium**
   - (a) Quais critérios avaliar antes de suspender sedação?
   - (b) Como conduzir avaliação CAM-ICU e responder a delirium hipo/hiperativo?
   - (c) Qual papel da família e da mobilização precoce?
   > 💡 *Gabarito orientador:* Garantir estabilidade hemodinâmica, PaO₂/FiO₂ adequado, analgesia controlada. Aplicar CAM-ICU após despertar; delirium hipoativo requer estímulo cognitivo, hiperativo pode demandar dexmedetomidina/antipsicótico. Família auxilia reorientação.

3. **Monitorização avançada e indicadores**
   - (a) Como usar BIS/EEG processado e integrar com escalas clínicas?
   - (b) Quais indicadores acompanhar (dias em sedação profunda não planejada, incidência de delirium, tempo até mobilização)?
   - (c) Como conduzir revisão mensal com equipe multiprofissional?
   > 💡 *Gabarito orientador:* BIS 40-60 para sedação cirúrgica, > 60 para sedação leve, correlacionar com RASS/CPOT. Indicadores: % tempo RASS na meta, delirium, uso de bloqueio neuromuscular. Reuniões com casos, dashboards e plano de ação.

---

## Questões de múltipla escolha (interativas)

> Rode `python -m exercicios.modulo_13_sedacao_analgesia`.

### Questão 1 — Meta RASS para ventilação mecânica estável
- A) +2
- B) 0 a +1
- C) −2 a 0
- D) −5
- E) +3
**Resposta correta:** C. Sedação leve a moderada otimiza ventilação e reduz delirium.

### Questão 2 — Hipertrigliceridemia com propofol
- A) Não requer intervenção até > 1000 mg/dL
- B) Trocar propofol por dexmedetomidina/quetamina
- C) Aumentar dose de propofol
- D) Administrar haloperidol
- E) Suspender analgesia
**Resposta correta:** B. Hipertrigliceridemia significativa exige reduzir ou trocar propofol por agentes alternativos.

### Questão 3 — Analgesia multimodal
- A) Depende exclusivamente de opioides
- B) Inclui paracetamol, cetamina, bloqueios regionais e técnicas não farmacológicas
- C) Contraindicada em trauma
- D) Dispensa avaliação de dor
- E) Inviabiliza mobilização
**Resposta correta:** B. Analgesia multimodal associa diferentes mecanismos para reduzir opioides.

### Questão 4 — Interrupção diária da sedação
- A) Contraindicada em todos os pacientes com noradrenalina
- B) Requer avaliação de estabilidade hemodinâmica e oxigenação
- C) Deve ocorrer apenas após extubação
- D) Dispensa comunicação com fisioterapia
- E) Não tem impacto em delirium
**Resposta correta:** B. Avaliar estabilidade antes de interromper e envolver equipe multiprofissional.

### Questão 5 — Manejo de delirium hiperativo
- A) Aumentar benzodiazepínicos indiscriminadamente
- B) Priorizar haloperidol IV, ambiente calmo e reorientação
- C) Restringir mobilização
- D) Suspender analgesia
- E) Alta imediata da UTI
**Resposta correta:** B. Delirium hiperativo exige antipsicótico, controle ambiental e suporte.

### Questão 6 — Dexmedetomidina
- A) Causa sempre hipertensão severa
- B) Permite sedação cooperativa com menor depressão respiratória
- C) Contraindicada em pacientes com sepsis
- D) Não impacta delirium
- E) Impede mobilização
**Resposta correta:** B. Dexmedetomidina favorece sedação responsiva e reduz delirium.

### Questão 7 — Escala CPOT
- A) Avalia apenas sedação
- B) Utiliza expressões faciais, movimentos, tensão muscular
- C) Não se aplica a pacientes intubados
- D) Níveis altos significam conforto
- E) Dispensa analgesia preemptiva
**Resposta correta:** B. CPOT avalia dor com indicadores comportamentais, útil em pacientes sedados.

### Questão 8 — Bundle ABCDEF
- A) Foca apenas em ventilação
- B) Inclui avaliação de dor, despertar diário, mobilização e envolvimento familiar
- C) Contraindica mobilização precoce
- D) Remove necessidade de sedação
- E) Aplica-se apenas a pacientes cirúrgicos
**Resposta correta:** B. Bundle ABCDEF estrutura cuidados integrados para reduzir delirium e melhorar desfechos.

---

## Afirmativas verdadeiro/falso (interativas)

1. Dexmedetomidina reduz incidência de delirium quando comparada a benzodiazepínicos. — **Verdadeiro.** Estudos apontam menor delirium.
2. Propofol em doses elevadas pode causar síndrome de infusão com acidose. — **Verdadeiro.** Monitorar lactato, CPK, triglicerídeos.
3. Analgesia adequada reduz tempo de ventilação mecânica. — **Verdadeiro.** Controle de dor melhora cooperação e ventilação.
4. Benzodiazepínicos são primeira linha para delirium hipoativo. — **Falso.** Preferir mobilização e antipsicóticos atípicos se necessário.
5. BIS 20 indica sedação leve. — **Falso.** BIS < 40 sugere sedação profunda.
6. Interrupção diária da sedação está associada a menor tempo de UTI. — **Verdadeiro.** Favorece extubação precoce.
7. CPOT > 3 indica controle analgésico inadequado. — **Verdadeiro.** Requer ajuste de analgesia.
8. Monitorização de pressão intraocular é desnecessária durante bloqueio neuromuscular. — **Falso.** Proteção ocular é essencial.
9. Quetamina pode ser usada como adjuvante analgésico em pacientes hemodinamicamente instáveis. — **Verdadeiro.** Aumenta pressão arterial moderadamente e poupa opioides.
10. Delirium hiperativo deve ser tratado com restrição física prolongada. — **Falso.** Restrições mínimas e monitorização são preferíveis.
11. Mobilização precoce faz parte do bundle ABCDEF. — **Verdadeiro.** Elemento "E" do bundle.
12. Uso prolongado de opioides não causa tolerância. — **Falso.** Exige estratégias de rotação e desmame.
13. Música terapêutica pode reduzir ansiedade e necessidade de sedação. — **Verdadeiro.** Estratégia não farmacológica útil.
14. Escala RASS deve ser registrada a cada turno apenas. — **Falso.** Recomenda-se monitorização frequente, especialmente após ajustes.
15. Sedação profunda contínua reduz risco de delirium. — **Falso.** Aumenta risco e prolonga ventilação.
