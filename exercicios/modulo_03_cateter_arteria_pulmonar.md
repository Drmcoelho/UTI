# Exercícios — Módulo 03 — Cateter de Artéria Pulmonar (Swan-Ganz)

## Como usar

1. Revise o material teórico em `docs/modulo_03_cateter_arteria_pulmonar.md` e os casos clínicos correspondentes.
2. Execute o notebook interativo e explore os simuladores associados ao módulo 03.
3. Rode o quiz interativo com `python -m exercicios.modulo_03_cateter_arteria_pulmonar` para treinar MCQ e V/F com pontuação em tempo real.
4. Utilize as questões dissertativas como base para discussões em grupo e portfólios reflexivos.

---

## Questões dissertativas

1. **Indicação e planejamento do cateter de artéria pulmonar**
   - (a) Quais perfis hemodinâmicos se beneficiam do Swan-Ganz?
   - (b) Quais exames laboratoriais e imagem devem anteceder o procedimento?
   - (c) Como elaborar checklist de segurança com a equipe?
   > 💡 *Gabarito orientador:* Utilizar em choque cardiogênico, choque misto refratário, hipertensão pulmonar complexa e pós-operatório de cirurgia cardíaca de alto risco. Solicitar coagulograma, hemograma, eletrólitos, radiografia de tórax e ecocardiograma recente. Checklist inclui verificação de materiais, calibragem de transdutores, monitor multiparamétrico, marcapasso externo e analgesia/sedação adequada.

2. **Interpretação integrada das curvas e parâmetros derivados**
   - (a) Como diferenciar curva de artéria pulmonar e PCP?
   - (b) Quais valores sugerem choque cardiogênico versus distributivo?
   - (c) Como correlacionar SvO₂, lactato e índice cardíaco?
   > 💡 *Gabarito orientador:* Curva de artéria pulmonar apresenta incisura dicrótica; PCP possui morfologia atrial com 'a' e 'v'. RVS elevada com PCP > 18 mmHg aponta cardiogênico; PCP baixa e RVS baixa indicam distributivo. SvO₂ < 60% com IC < 2,2 L/min/m² e lactato elevado reforçam hipoperfusão.

3. **Estratégias para retirada segura do cateter**
   - (a) Quais metas clínicas e laboratoriais devem ser atingidas?
   - (b) Como monitorar sinais de complicação durante a retirada?
   - (c) Que documentação e educação ao time são necessários após remoção?
   > 💡 *Gabarito orientador:* Exigir PAM ≥ 65-70 mmHg sem escalonamento, IC ≥ 2,2 L/min/m², SvO₂ ≥ 65%, PCP adequada (< 18 mmHg) e lactato < 2 mmol/L. Monitorar arritmias, resistência durante tração e sangramento. Documentar horário, medidas finais, condições do paciente e orientações para vigilância nas próximas horas.

---

## Questões de múltipla escolha (interativas)

> Execute `python -m exercicios.modulo_03_cateter_arteria_pulmonar` e registre sua pontuação.

### Questão 1 — Qual sequência correta para a passagem do cateter de artéria pulmonar?
- A) Introdução na veia femoral → átrio direito → ventrículo direito → artéria pulmonar → wedge
- B) Introdução na veia subclávia → ventrículo direito → átrio direito → artéria pulmonar
- C) Introdução na veia jugular → artéria pulmonar → ventrículo direito → átrio direito
- D) Introdução na veia femoral → átrio direito → artéria pulmonar → ventrículo esquerdo
- E) Introdução na veia subclávia → artéria pulmonar → wedge → ventrículo esquerdo
**Resposta correta:** A. A sequência habitual é átrio direito, ventrículo direito, artéria pulmonar e oclusão (PCP) com balão insuflado ao final.

### Questão 2 — Qual das situações abaixo contraindica temporariamente a inserção do CAP?
- A) Paciente com uso de anticoagulação profilática
- B) Bloqueio de ramo esquerdo prévio
- C) Choque cardiogênico com ECMO
- D) Hipotermia terapêutica
- E) Uso de drogas inotrópicas
**Resposta correta:** B. CAP pode precipitar bloqueio AV completo em pacientes com BRE; considerar marca-passo temporário antes da passagem.

### Questão 3 — PCP 26 mmHg, RVS 1.400 dyn·s·cm⁻⁵ e IC 1,8 L/min/m² sugerem
- A) Choque distributivo
- B) Choque cardiogênico
- C) Hipovolemia
- D) Choque obstrutivo
- E) Situação normal
**Resposta correta:** B. PCP elevada, RVS alta e IC baixo caracterizam choque cardiogênico com congestão pulmonar importante.

### Questão 4 — Durante insuflação do balão, a curva apresenta onda ventriculosa sustentada. Conduta imediata?
- A) Prosseguir com a insuflação até desaparecer
- B) Desinsuflar imediatamente e recuar 1-2 cm
- C) Aumentar fluxo de oxigênio
- D) Administrar vasodilatador pulmonar
- E) Retirar cateter e reinserir pelo outro lado
**Resposta correta:** B. Onda ventriculosa indica posicionamento em ventrículo direito; desinsuflar e reposicionar para evitar perfuração.

### Questão 5 — Qual cálculo correto da RVS considerando PAM 70 mmHg, PVC 12 mmHg, DC 4 L/min?
- A) RVS = 80 × (PAM − PVC) / DC
- B) RVS = PAM / DC
- C) RVS = (PAM × DC) / 80
- D) RVS = 60 × (PVC − PAM) / DC
- E) RVS = (PAM − PVC) × DC
**Resposta correta:** A. A fórmula padrão é RVS = 80 × (PAM − PVC) / DC, resultando em 1.040 dyn·s·cm⁻⁵ nesse exemplo.

### Questão 6 — Queda abrupta da SvO₂ para 52% com IC estável sugere
- A) Aumento do consumo de oxigênio
- B) Erro de calibração
- C) Aumento do débito cardíaco
- D) Perfuração de artéria pulmonar
- E) Tamponamento cardíaco
**Resposta correta:** A. SvO₂ reduzida com IC estável indica aumento do consumo (febre, agitação) ou queda na saturação arterial; investigar causa clínica.

### Questão 7 — Qual achado sugere hipertensão pulmonar pré-capilar?
- A) PCP 26 mmHg e PAP média 28 mmHg
- B) PCP 12 mmHg e PAP média 35 mmHg
- C) PCP 8 mmHg e PAP média 20 mmHg
- D) PCP 18 mmHg e PAP média 24 mmHg
- E) PCP 10 mmHg e PAP média 22 mmHg
**Resposta correta:** B. PAP média ≥ 25 mmHg com PCP ≤ 15 mmHg caracteriza hipertensão pulmonar pré-capilar; PAP 35 e PCP 12 cumprem o critério.

### Questão 8 — Quando considerar retirada do CAP após estabilização?
- A) Após redução de lactato, mas ainda em altas doses de vasopressor
- B) Quando critérios clínicos e hemodinâmicos estáveis ≥ 24h sem ajustes
- C) Imediatamente após normalizar a SvO₂
- D) Quando o paciente inicia mobilização passiva
- E) Assim que o débito urinário melhora
**Resposta correta:** B. Retirada segura ocorre após 24h sem ajustes, com metas de PAM, PCP, SvO₂ e IC consolidadas e sem novas intervenções planejadas.

---

## Afirmativas verdadeiro/falso (interativas)

> Disponível no mesmo script interativo: `python -m exercicios.modulo_03_cateter_arteria_pulmonar`.

1. PCP representa estimativa indireta da pressão de átrio esquerdo.
   - **Gabarito:** Verdadeiro. Em condições sem obstrução, PCP reflete pressão diastólica final do ventrículo esquerdo.

2. Balão deve permanecer insuflado continuamente para prevenir deslocamento.
   - **Gabarito:** Falso. Balão deve ser desinsuflado após a medida; insuflação contínua aumenta risco de isquemia pulmonar.

3. SvO₂ < 60% com lactato elevado sugere aporte insuficiente de oxigênio.
   - **Gabarito:** Verdadeiro. Combinação indica má perfusão e deve levar à otimização de débito ou oferta de O₂.

4. PVC elevada isoladamente confirma sobrecarga de volume.
   - **Gabarito:** Falso. PVC isolada é inespecífica; é necessário integrar com outros parâmetros e exame físico.

5. A curva wedge normal possui ondas 'a' e 'v' proeminentes.
   - **Gabarito:** Verdadeiro. Formato atrial ajuda a diferenciar de curva ventricular durante posicionamento.

6. Injetar solução fria no termistor permite calcular débito cardíaco por termodiluição.
   - **Gabarito:** Verdadeiro. A queda de temperatura registrada produz curva utilizada no cálculo do débito.

7. RVS baixa e PCP alta caracterizam choque distributivo.
   - **Gabarito:** Falso. Choque distributivo cursa com PCP baixa; PCP alta sugere componente cardiogênico.

8. O CAP não deve ser utilizado em pacientes com prótese valvar.
   - **Gabarito:** Falso. Próteses não contraindicam; considerar risco individual e técnica apurada.

9. Hipertensão pulmonar severa aumenta risco de ruptura arterial durante passagem do cateter.
   - **Gabarito:** Verdadeiro. Fragilidade vascular e pressões elevadas elevam risco de hemorragia.

10. Ao inflar o balão, o volume máximo recomendado é 1,5 mL.
   - **Gabarito:** Verdadeiro. Exceder 1,5 mL aumenta risco de ruptura vascular e wedge falso.

11. Índice cardíaco é calculado dividindo o débito cardíaco pela superfície corporal.
   - **Gabarito:** Verdadeiro. IC (L/min/m²) permite comparar débito ajustado ao tamanho corporal.

12. Se a curva wedge não aparece, deve-se avançar o cateter com balão desinsuflado.
   - **Gabarito:** Falso. Avançar desinsuflado aumenta risco de perfuração; avançar com balão insuflado de forma controlada.

13. CAP fornece medidas contínuas de saturação venosa mista quando equipado com fibra óptica.
   - **Gabarito:** Verdadeiro. Modelos modernos oferecem SvO₂ contínua para trending em tempo real.

14. Após retirada, é dispensável monitorar o sítio de inserção.
   - **Gabarito:** Falso. É obrigatório monitorar sangramento, hematoma e sinais de infecção nas horas seguintes.

15. Elevação súbita da pressão de artéria pulmonar pode indicar oclusão do cateter.
   - **Gabarito:** Verdadeiro. Revisar posicionamento e descartar trombo ou looping do cateter.
