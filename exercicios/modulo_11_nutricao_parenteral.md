# Exercícios — Módulo 11 — Nutrição Parenteral Total (NPT)

## Como usar

1. Revise o guia teórico [`docs/modulo_11_nutricao_parenteral.md`](../docs/modulo_11_nutricao_parenteral.md) e execute o notebook correspondente para dominar cálculos automatizados.
2. Explore o simulador `simuladores/modulo_11_nutricao_parenteral.py` para praticar cenários de refeeding, ajustes de macro/micronutrientes e monitorização.
3. Execute o quiz interativo com `python -m exercicios.modulo_11_nutricao_parenteral` para registrar sua pontuação nas MCQ e V/F.
4. Utilize as questões dissertativas para elaborar planos nutricionais, submetendo ao preceptor para feedback detalhado.

---

## Questões dissertativas

1. **Prescrição completa da NPT nas primeiras 72h**
   - (a) Como definir peso e calorias alvo (incluindo proteínas, lipídios e carboidratos)?
   - (b) Quais ajustes diários devem ser feitos considerando eletrólitos e glicemia?
   - (c) Como escalonar a oferta para evitar síndrome de realimentação?
   > 💡 *Gabarito orientador:* Utilize peso ajustado/ideal, distribua 20% proteína, 30% lipídio, 50% carboidrato, com 1,5-2 g/kg de proteína. Reavalie Na, K, Mg, P a cada 12-24h, ajuste insulina conforme glicemia. Escalone 60→80→100% da meta se eletrólitos estáveis, suplementando tiamina.

2. **Gerenciamento de complicações metabólicas**
   - (a) Como monitorar triglicerídeos, função hepática e equilíbrio ácido-base?
   - (b) Quais intervenções aplicar quando TG > 400 mg/dL ou transaminases sobem 3x o limite?
   - (c) Qual plano para hiperglicemia persistente > 180 mg/dL apesar de insulina basal?
   > 💡 *Gabarito orientador:* Dosar TG e enzimas hepáticas 2-3x/semana, avaliar acidose metabólica/lática. Suspender lipídio por 24-48h ou reduzir 50%, investigar colestase, ajustar carboidrato. Implementar protocolo de insulina IV com ajustes a cada 1-2h e revisão da taxa de dextrose.

3. **Transição e alta**
   - (a) Quais critérios indicam possibilidade de transição para nutrição enteral parcial?
   - (b) Como preparar equipe e família para home parenteral, incluindo educação e monitorização?
   - (c) Quais indicadores de qualidade acompanhar após alta (infecção, reinternação, metas calóricas)?
   > 💡 *Gabarito orientador:* Considerar transição quando TGI funcional, tolerância a dieta > 60% da meta. Para home parenteral, envolver enfermagem especializada, farmácia, nutricionista, garantir técnica asséptica, calendário de exames e monitorar infecção de cateter, peso, marcadores nutricionais.

---

## Questões de múltipla escolha (interativas)

> Execute `python -m exercicios.modulo_11_nutricao_parenteral` e registre sua pontuação.

### Questão 1 — Indicação de NPT exclusiva
- A) Resíduos gástricos 150 mL
- B) Cirurgia bariátrica há 48h
- C) Fístula entérica de alto débito com íleo prolongado
- D) Pancreatite leve tolerando dieta oral
- E) Diarreia por antibiótico
**Resposta correta:** C. Fístula de alto débito com íleo prolongado impede nutrição enteral efetiva.

### Questão 2 — Distribuição calórica
- A) 70% carboidrato, 10% proteína, 20% lipídio
- B) 40% carboidrato, 40% proteína, 20% lipídio
- C) 60% carboidrato, 20% proteína, 20% lipídio
- D) 30% carboidrato, 30% proteína, 40% lipídio
- E) 80% carboidrato, 10% proteína, 10% lipídio
**Resposta correta:** C. Distribuição clássica garante aporte proteico adequado e balanço não proteico/nitrogênio.

### Questão 3 — Osmolaridade limite para acesso periférico
- A) 600 mOsm/L
- B) 700 mOsm/L
- C) 900 mOsm/L
- D) 1100 mOsm/L
- E) 1500 mOsm/L
**Resposta correta:** B. Acima de 700-750 mOsm/L recomenda-se via central para evitar flebite.

### Questão 4 — Prevenção de refeeding
- A) Iniciar com 100% das calorias
- B) Suspender tiamina
- C) Suplementar fósforo, magnésio e tiamina antes da NPT
- D) Aumentar lipídios para 50%
- E) Infundir dextrose em bolus
**Resposta correta:** C. Reposição de micronutrientes e escalonamento gradual previnem refeeding.

### Questão 5 — Ajuste diante de TG 450 mg/dL
- A) Aumentar infusão de lipídio
- B) Suspender lipídio temporariamente
- C) Reduzir dextrose e aumentar lipídio
- D) Aumentar velocidade da bomba
- E) Administrar bicarbonato
**Resposta correta:** B. Suspender lipídio por 24-48h até normalização dos triglicerídeos.

### Questão 6 — Monitorização de eletrólitos
- A) Dosar Na e K semanalmente é suficiente
- B) Mg e fósforo devem ser avaliados diariamente nas primeiras 72h
- C) Cloreto não impacta acidose
- D) Cálcio não deve ser considerado
- E) Bicarbonato não influencia osmolaridade
**Resposta correta:** B. Monitorização diária de Mg e P previne refeeding e complicações neuromusculares.

### Questão 7 — Infecção relacionada ao cateter
- A) Trocar equipo a cada 96h
- B) Não há necessidade de curativo estéril
- C) Realizar curativo a cada 48h ou se sujo
- D) Infusão contínua dispensa técnica asséptica
- E) NPT pode ser infundida em cateter usado para drogas vasoativas
**Resposta correta:** C. Curativos estéreis a cada 48h e manipulação asséptica são obrigatórios.

### Questão 8 — Critério para home parenteral
- A) Necessidade < 500 kcal/dia
- B) Acesso venoso temporário
- C) Equipe treinada e paciente estável
- D) Falta de suporte familiar
- E) Prescrição sem revisão semanal
**Resposta correta:** C. Home parenteral exige estabilidade clínica e suporte multiprofissional treinado.

---

## Afirmativas verdadeiro/falso (interativas)

> Disponível no mesmo script interativo: `python -m exercicios.modulo_11_nutricao_parenteral`.

1. NPT exclusiva é indicada quando nutrição enteral não alcança > 60% das necessidades em 7 dias. — **Verdadeiro.** Diretrizes recomendam NPT precoce em pacientes de alto risco quando enteral insuficiente.
2. A relação caloria não proteica/nitrogênio deve ficar abaixo de 60:1. — **Falso.** Ideal 100-120:1 para equilibrar catabolismo.
3. Tiamina deve ser administrada antes e durante os primeiros dias de NPT. — **Verdadeiro.** Previne encefalopatia e refeeding.
4. Cateter dedicado à NPT pode ser usado para coletar gasometrias. — **Falso.** Uso exclusivo reduz contaminação.
5. Osmolaridade elevada aumenta risco de trombose venosa. — **Verdadeiro.** Soluções hipertônicas sem via central causam flebite e trombose.
6. Lipídios devem ser infundidos rapidamente para reduzir tempo de manipulação. — **Falso.** Infusão lenta (12-24h) reduz complicações metabólicas.
7. Síndrome de refeeding cursa com hipofosfatemia, hipomagnesemia e retenção hídrica. — **Verdadeiro.** Distúrbios eletrolíticos são marcantes.
8. Ajustes de insulina não são necessários em NPT. — **Falso.** Protocolo glicêmico rigoroso é essencial.
9. Micronutrientes podem ser omitidos nos primeiros 3 dias. — **Falso.** Devem ser administrados desde o início.
10. Verificar sinais flogísticos do cateter diariamente faz parte do bundle. — **Verdadeiro.** Inspeção visual diária previne infecção.
11. NPT suplementar associa-se a menor mortalidade em pacientes cirúrgicos com risco nutricional elevado. — **Verdadeiro.** Evidências suportam suplementação precoce.
12. Não há necessidade de controle de balanço hídrico com NPT. — **Falso.** Volume total deve ser integrado ao balanço.
13. Hipertrigliceridemia requer suspensão temporária de lipídios. — **Verdadeiro.** TG > 400-500 mg/dL exige ajuste.
14. Fósforo sérico normal dispensa monitorização após início da NPT. — **Falso.** Pode cair rapidamente, exigindo vigilância contínua.
15. A técnica de infusão cíclica pode ser considerada para pacientes estáveis. — **Verdadeiro.** Permite períodos sem infusão, melhorando qualidade de vida.
