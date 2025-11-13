# Exercícios — Módulo 12 — Controle Glicêmico Avançado

## Como usar

1. Revise o guia [`docs/modulo_12_controle_glicemico.md`](../docs/modulo_12_controle_glicemico.md) e execute o notebook para dominar gráficos de tendência e planilhas de auditoria.
2. Utilize o simulador `simuladores/modulo_12_controle_glicemico.py` para praticar ajustes dinâmicos da infusão de insulina em múltiplos cenários.
3. Rode o quiz com `python -m exercicios.modulo_12_controle_glicemico` para registrar pontuação nas MCQ e V/F.
4. Responda às questões dissertativas em portfólio reflexivo, correlacionando com indicadores institucionais.

---

## Questões dissertativas

1. **Protocolos baseados em taxa de variação**
   - (a) Como calcular taxa de variação glicêmica e ajustar infusão para alcançar meta 110-160 mg/dL?
   - (b) Quais adaptações fazer em pacientes com nutrição parenteral contínua e corticoterapia?
   - (c) Como documentar ajustes e garantir checagem dupla?
   > 💡 *Gabarito orientador:* Taxa = (glicemia atual − anterior)/tempo; ajustar de acordo com tabelas institucionais. Em NPT/corticoide, considerar fator de sensibilidade reduzido e monitorização horária. Checagem dupla com enfermagem, registro no prontuário e no dashboard.

2. **Prevenção e manejo de hipoglicemia**
   - (a) Quais gatilhos identificar (interrupção de dieta, erro de bomba, insuficiência renal)?
   - (b) Como estruturar protocolo de resgate e reavaliação pós-evento?
   - (c) Que indicadores acompanhar para melhorar segurança?
   > 💡 *Gabarito orientador:* Monitorar pausas de dieta, velocidades erradas, uso de beta-bloqueadores. Resgate com dextrose IV, reavaliação 10-15 min, ajuste do protocolo e notificação. Indicadores: % medições < 70 mg/dL, tempo de correção, eventos recorrentes.

3. **Auditoria e melhoria contínua**
   - (a) Como calcular tempo na meta (Time in Range) e variabilidade glicêmica?
   - (b) Quais estratégias para feedback multiprofissional (reuniões, dashboards, educação)?
   - (c) Como integrar dados com protocolos de nutrição e sedação?
   > 💡 *Gabarito orientador:* Time in Range = medições dentro da meta / total. Variabilidade = desvio padrão ou coeficiente de variação. Feedback com reuniões semanais, dashboards e educação focada. Integrar dados com nutrição/sedação para identificar correlações.

---

## Questões de múltipla escolha (interativas)

> Execute `python -m exercicios.modulo_12_controle_glicemico`.

### Questão 1 — Meta glicêmica padrão em pacientes críticos
- A) 80-110 mg/dL
- B) 90-120 mg/dL
- C) 110-140 mg/dL
- D) 140-180 mg/dL
- E) 180-220 mg/dL
**Resposta correta:** D. Diretrizes recomendam alvo 140-180 mg/dL na maioria dos pacientes críticos.

### Questão 2 — Ajuste baseado em taxa de variação
- A) Variação +10 mg/dL/h sugere reduzir infusão
- B) Variação +40 mg/dL/h demanda aumento da infusão
- C) Variação −20 mg/dL/h exige aumento
- D) Variação −60 mg/dL/h sem sintomas não requer ação
- E) Taxa de variação é irrelevante
**Resposta correta:** B. Elevação rápida requer intensificar a infusão conforme protocolo.

### Questão 3 — Prevenção de hipoglicemia durante interrupção de dieta
- A) Manter infusão igual independente da dieta
- B) Reduzir 50% ou suspender conforme duração da pausa
- C) Administrar bolo de insulina
- D) Aumentar alvo glicêmico para 250 mg/dL
- E) Sem necessidade de monitorização
**Resposta correta:** B. Pausas exigem redução ou suspensão temporária e monitorização intensificada.

### Questão 4 — Fator de sensibilidade à insulina
- A) 1500/dose diária total de insulina IV
- B) 1800/dose total de insulina subcutânea
- C) 500/dose de insulina basal
- D) 100/dose de insulina prandial
- E) Não existe cálculo aplicável em UTI
**Resposta correta:** B. Regra 1800 auxilia estimar queda de glicemia por unidade em regime basal-bolus, adaptável ao contexto crítico.

### Questão 5 — Indicador de qualidade prioritário
- A) Número de seringas utilizadas por plantão
- B) Tempo na meta glicêmica
- C) Volume de soro glicosado infundido
- D) Número de folhas de prontuário
- E) Quantidade de refeições fornecidas
**Resposta correta:** B. Tempo na meta (Time in Range) correlaciona-se com desfechos clínicos.

### Questão 6 — Hipoglicemia grave (< 40 mg/dL)
- A) Não requer registro
- B) Deve ser registrada e analisada em reunião de segurança
- C) Pode ser ignorada se paciente assintomático
- D) Conduz automaticamente à suspensão definitiva de insulina
- E) Indica sempre infecção
**Resposta correta:** B. Hipoglicemias graves devem ser notificadas e analisadas sistematicamente.

### Questão 7 — Uso de dexmedetomidina
- A) Aumenta invariavelmente glicemia
- B) Reduz necessidade de monitorização
- C) Pode mascarar sinais de hipoglicemia (bradicardia)
- D) Elimina necessidade de protocolo de insulina
- E) Substitui nutrição adequada
**Resposta correta:** C. Sedativos podem mascarar sinais autonômicos, exigindo vigilância maior.

### Questão 8 — Integração com nutrição parenteral
- A) Não há impacto sobre a glicemia
- B) NPT demanda insulina adicionada diretamente ao saco sem reavaliação
- C) A taxa de dextrose influencia necessidade de insulina
- D) Lipídios sempre dispensam monitorização glicêmica
- E) Eletrólitos controlam glicemia
**Resposta correta:** C. A velocidade de dextrose e calorias não proteicas define necessidade de insulina.

---

## Afirmativas verdadeiro/falso (interativas)

1. Protocolos de insulina IV devem incluir checagem dupla em cada ajuste. — **Verdadeiro.** Reduz erros de medicação.
2. Meta 80-110 mg/dL é recomendada rotineiramente em todos os pacientes críticos. — **Falso.** Associada a maior hipoglicemia; usar 140-180 mg/dL.
3. Variabilidade glicêmica elevada aumenta mortalidade em UTI. — **Verdadeiro.** Flutuações amplas correlacionam-se com piores desfechos.
4. Corticoides elevam glicemia e exigem intensificação da insulina. — **Verdadeiro.** Resistência insulínica aumenta.
5. Tempo na meta é calculado contando medições dentro do alvo dividido pelo total. — **Verdadeiro.** Indicador simples e objetivo.
6. Pausas de dieta enteral não influenciam glicemia. — **Falso.** Podem causar hipoglicemia se infusão de insulina mantida.
7. Ajustar nutrição parenteral não impacta controle glicêmico. — **Falso.** Alterações calóricas mudam demanda de insulina.
8. Hipoglicemia deve ser comunicada à equipe multiprofissional. — **Verdadeiro.** Permite intervenção coordenada.
9. Dexmedetomidina não interfere no metabolismo da glicose. — **Falso.** Pode reduzir resposta simpática, mascarando sintomas.
10. Monitorização arterial contínua dispensa glicemia capilar. — **Falso.** Necessário calibrar e correlacionar com capilares/venosos.
11. Pacientes em TSR contínua requerem ajustes específicos de insulina. — **Verdadeiro.** Mudanças no clearance e aporte impactam doses.
12. Registrar hipoglicemias apenas quando sintomáticas é suficiente. — **Falso.** Assintomáticas também exigem registro e análise.
13. Indicadores devem ser revisados mensalmente no mínimo. — **Verdadeiro.** Garante melhoria contínua.
14. Uso de agonistas beta-2 reduz glicemia, dispensando monitorização. — **Falso.** Podem elevar glicemia; monitorização permanece necessária.
15. Interrupções frequentes de dieta requerem revisão do protocolo de insulina. — **Verdadeiro.** Ajustes evitam hipoglicemias repetidas.
