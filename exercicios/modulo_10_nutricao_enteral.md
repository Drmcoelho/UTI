# Exercícios — Módulo 10 — Nutrição Enteral em Pacientes Críticos

## Como usar

1. Revise o guia [`docs/modulo_10_nutricao_enteral.md`](../docs/modulo_10_nutricao_enteral.md) e o protocolo em `recursos/10_nutricao_enteral/`.
2. Planeje metas com `simuladores/modulo_10_nutricao_enteral.py` para calcular calorias, proteínas e ajustes de taxa.
3. Execute `python -m exercicios.modulo_10_nutricao_enteral` para praticar MCQ e V/F.
4. Use as questões dissertativas em reuniões multiprofissionais (nutrição, enfermagem, fisioterapia, intensivistas).

---

## Questões dissertativas

1. **Planejamento nutricional em paciente de alto risco**
   - (a) Como calcular necessidades calóricas e proteicas personalizadas?
   - (b) Qual estratégia de progressão da dieta para atingir metas em 72h?
   - (c) Quais indicadores devem ser monitorados diariamente?
   > 💡 *Gabarito orientador:* Utilizar 25-30 kcal/kg ajustados por calorimetria quando possível e 1,5-2 g/kg de proteína considerando estresse metabólico. Progressão escalonada iniciando com 25 mL/h e aumento de 10-20 mL/h a cada 6h se resíduos < 500 mL e hemodinâmica estável. Monitorar balanço nitrogenado, glicemia, eletrólitos, resíduos, evacuações, peso e marcadores inflamatórios.

2. **Gestão de intolerância gastrointestinal**
   - (a) Quais causas avaliar diante de resíduos elevados?
   - (b) Quais intervenções farmacológicas podem ser utilizadas?
   - (c) Quando indicar sonda pós-pilórica?
   > 💡 *Gabarito orientador:* Revisar posição da sonda, uso de opioides/sedação, distúrbios eletrolíticos, íleo e infecções. Utilizar pró-cinéticos (metoclopramida, eritromicina), ajustar velocidade, considerar naloxona enteral e fórmulas com fibra. Indicar pós-pilórica se resíduos > 500 mL persistentes, alto risco de aspiração ou ventilação prolongada.

3. **Integração multiprofissional e documentação**
   - (a) Como envolver nutrição, enfermagem e fisioterapia no plano?
   - (b) Quais registros são mandatórios para rastreabilidade?
   - (c) Como comunicar interrupções e retomadas da dieta?
   > 💡 *Gabarito orientador:* Rounds multiprofissionais com metas claras, posicionamento adequado (30-45°) e checklist de tolerância. Registros obrigatórios: volume prescrito/infundido, resíduos, evacuações, suplementos, eventos adversos e justificativas de pausas. Documentar horário, motivo, responsável e plano de reinício com metas reajustadas.

---

## Questões de múltipla escolha (interativas)

> Execute `python -m exercicios.modulo_10_nutricao_enteral` para ver feedback.

### Questão 1 — Paciente 70 kg, alvo 30 kcal/kg/dia. Meta calórica?
- A) 1500 kcal
- B) 1800 kcal
- C) 2100 kcal
- D) 2400 kcal
- E) 2700 kcal
**Resposta correta:** C. 30 kcal/kg × 70 kg = 2100 kcal.

### Questão 2 — Meta proteica diária para 80 kg (1,8 g/kg)?
- A) 96 g
- B) 120 g
- C) 144 g
- D) 180 g
- E) 200 g
**Resposta correta:** C. 1,8 g/kg × 80 kg = 144 g.

### Questão 3 — Limiar de resíduo gástrico que exige intervenção segundo ASPEN/ESPEN?
- A) >150 mL
- B) >250 mL
- C) >500 mL
- D) >700 mL
- E) >1000 mL
**Resposta correta:** C. Resíduos > 500 mL de forma repetida requerem ajustes.

### Questão 4 — Suplemento indicado em grandes queimados para imunonutrição?
- A) Glutamina
- B) Vitamina K
- C) Cálcio
- D) Bicarbonato
- E) Vitamina D
**Resposta correta:** A. Glutamina enteral auxilia suporte imunológico.

### Questão 5 — Alvo glicêmico recomendado em pacientes críticos com dieta enteral?
- A) 80-110 mg/dL
- B) 110-140 mg/dL
- C) 140-180 mg/dL
- D) 180-220 mg/dL
- E) >220 mg/dL
**Resposta correta:** C. Diretrizes sugerem 140-180 mg/dL.

### Questão 6 — Abordagem que reduz risco de aspiração durante infusão?
- A) Cabeceira a 15°
- B) Infusão em bolus
- C) Posicionamento a 30-45°
- D) Suspender pró-cinéticos
- E) Reduzir hidratação
**Resposta correta:** C. Cabeceira elevada 30-45° reduz refluxo e aspiração.

### Questão 7 — Paciente em noradrenalina 0,1 mcg/kg/min e dieta enteral. Conduta?
- A) Suspender dieta
- B) Manter dieta com monitorização
- C) Aumentar rapidamente velocidade
- D) Migrar para parenteral
- E) Adicionar lipídios IV
**Resposta correta:** B. Com vasopressor estável, manter enteral com vigilância de perfusão.

### Questão 8 — Parâmetro que confirma adequação proteica ao final da semana?
- A) Queda do peso
- B) Aumento da creatinina
- C) Balanço nitrogenado próximo de zero
- D) Pré-albumina em queda
- E) PCR elevada
**Resposta correta:** C. Balanço nitrogenado ≈ 0 indica oferta proteica adequada.

---

## Afirmativas verdadeiro/falso (interativas)

> Disponível no mesmo script interativo.

1. Escalas NUTRIC ajudam a definir prioridade da terapia nutricional. — **Verdadeiro.** Estratificam risco e orientam metas agressivas.
2. Resíduos gástricos devem ser mensurados apenas uma vez ao dia. — **Falso.** Nas primeiras 48-72h recomenda-se avaliar a cada 4-6h.
3. Vasopressores são contraindicação absoluta à nutrição enteral. — **Falso.** Doses baixas a moderadas permitem enteral com vigilância.
4. Fibra solúvel pode ajudar no manejo de diarreia. — **Verdadeiro.** Melhora consistência fecal e microbiota.
5. Interrupções prolongadas (>2h) devem ser evitadas. — **Verdadeiro.** Atrasam metas calóricas.
6. Nutrição enteral deve ser suspensa definitivamente diante do primeiro episódio de diarreia. — **Falso.** Investigar causas e ajustar fórmula.
7. Cálcio sérico é o principal marcador de tolerância enteral. — **Falso.** Avaliar resíduos, distensão, evacuações e aspiração.
8. Pré-albumina isoladamente não deve guiar decisão diária. — **Verdadeiro.** Sofre influência inflamatória.
9. Nutrição enteral precoce (<24h) reduz infecção em queimados. — **Verdadeiro.** Menor translocação bacteriana.
10. Sonda pós-pilórica elimina risco de aspiração. — **Falso.** Reduz mas não elimina; manter cabeceira elevada.
11. Suplementação de zinco é desnecessária em grandes queimados. — **Falso.** Essencial para cicatrização/imunidade.
12. Controle glicêmico com insulina IV pode ser necessário para atingir metas. — **Verdadeiro.** Infusão contínua ajusta melhor.
13. Documentar motivo das interrupções é opcional. — **Falso.** Rastreabilidade exige registro detalhado.
14. Ferramentas digitais de prescrição ajudam a reduzir erros de volume. — **Verdadeiro.** Alarmes e cálculos automáticos evitam divergências.
15. Nutrição enteral deve ser conduzida apenas pela equipe de nutrição. — **Falso.** Responsabilidade compartilhada entre equipe multiprofissional.
