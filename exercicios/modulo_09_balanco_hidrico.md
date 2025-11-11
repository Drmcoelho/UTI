# Exercícios — Módulo 09 — Balanço Hídrico e Controle de Volemia

## Como usar

1. Revise o guia [`docs/modulo_09_balanco_hidrico.md`](../docs/modulo_09_balanco_hidrico.md) e o template em `recursos/09_balanco_hidrico/`.
2. Utilize `simuladores/modulo_09_balanco_hidrico.py` para calcular fração de sobrecarga, metas e respostas a diuréticos.
3. Execute `python -m exercicios.modulo_09_balanco_hidrico` para praticar MCQ/VF com pontuação.
4. Explore as questões dissertativas em reuniões com nefrologia e equipe multiprofissional.

---

## Questões dissertativas

1. **Estratégias avançadas de remoção de fluido**
   - (a) Como calcular a fração de sobrecarga hídrica e definir meta diária?
   - (b) Quais combinações farmacológicas compõem o diurético sequencial?
   - (c) Quando migrar para ultrafiltração contínua?
   > 💡 *Gabarito orientador:* Fração = balanço acumulado/peso ideal; metas costumam ser 1-1,5 L/dia ajustadas à perfusão. Diurético sequencial: furosemida contínua, tiazídicos, acetazolamida e antagonistas de aldosterona conforme necessidade. Ultrafiltração quando sobrecarga >10%, diurese <0,5 mL/kg/h persistente ou congestão orgânica refratária.

2. **Integração de ferramentas de monitorização**
   - (a) Como interpretar score VEXUS com IVC e B-lines?
   - (b) Quais marcadores laboratoriais monitorar durante remoção agressiva?
   - (c) Como apresentar dados em rounds multiprofissionais?
   > 💡 *Gabarito orientador:* VEXUS avalia doppler hepático, portal e intrarrenal; grau elevado com IVC dilatada e B-lines difusas indica congestão severa. Monitorar eletrólitos, osmolaridade, lactato, função hepática/renal e biomarcadores cardíacos. Apresentar dashboards com balanço, peso, ultrassom e laboratório para decisões compartilhadas.

3. **Governança e segurança do balanço**
   - (a) Quais elementos compõem o checklist diário de balanço?
   - (b) Como documentar entradas e saídas de forma confiável?
   - (c) Quais gatilhos exigem revisão imediata do plano?
   > 💡 *Gabarito orientador:* Checklist: peso diário, balanço acumulado, metas 24h, sinais de hipoperfusão, monitorização hemodinâmica e alinhamento multiprofissional. Registros horários com dupla checagem enfermagem/médico e uso de sistema eletrônico. Revisar se lactato sobe, PAM cai, débito urinário reduz ou surgem alterações neurológicas/hepáticas.

---

## Questões de múltipla escolha (interativas)

> Utilize `python -m exercicios.modulo_09_balanco_hidrico` para feedback.

### Questão 1 — Paciente 70 kg com ganho de 5 L em 48h. Fração de sobrecarga?
- A) 3%
- B) 5%
- C) 7%
- D) 9%
- E) 12%
**Resposta correta:** C. 5 L/70 kg ≈ 7% — valor clinicamente relevante.

### Questão 2 — Qual achado no VEXUS indica congestão hepática grave?
- A) Fluxo portal contínuo anterógrado
- B) Fluxo hepático tripásico
- C) Fluxo portal reverso
- D) Fluxo renal monofásico
- E) IVC colabada
**Resposta correta:** C. Fluxo portal reverso é marcador de congestão severa.

### Questão 3 — Durante diurético sequencial, qual eletrólito monitorar com maior frequência?
- A) Cálcio
- B) Magnésio
- C) Sódio
- D) Potássio
- E) Fósforo
**Resposta correta:** D. Perdas de potássio são importantes e devem ser repostas.

### Questão 4 — Qual critério favorece ultrafiltração contínua em vez de intermitente?
- A) Hipotensão instável
- B) Necessidade de remoção rápida
- C) Sódio 150 mEq/L
- D) Balanço negativo leve
- E) Diurese 1 mL/kg/h
**Resposta correta:** A. Hemodinâmica instável tolera melhor ultrafiltração contínua.

### Questão 5 — Objetivo de balanço seguro em transplante hepático com congestão severa?
- A) −3 L/dia
- B) −2 L/dia
- C) −1,5 L/dia
- D) 0 L/dia
- E) +0,5 L/dia
**Resposta correta:** C. Remoções moderadas 1-1,5 L/dia equilibram perfusão e descongestão.

### Questão 6 — Marcador laboratorial de hipoperfusão hepática durante remoção agressiva?
- A) AST/ALT em queda
- B) Bilirrubina indireta baixa
- C) Lactato crescente
- D) Fosfatase alcalina estável
- E) Albumina elevada
**Resposta correta:** C. Lactato elevado sinaliza hipoperfusão sistêmica/hepática.

### Questão 7 — Pressão negativa elevada no circuito de ultrafiltração contínua. Conduta?
- A) Aumentar taxa de ultrafiltração
- B) Flushing do cateter e avaliar posição
- C) Suspender anticoagulação
- D) Trocar membrana imediatamente
- E) Ignorar se PAM estável
**Resposta correta:** B. Pressão negativa sugere obstrução; lavar e reposicionar antes de aumentar taxa.

### Questão 8 — Queda abrupta de débito urinário e PAM durante remoção sugere:
- A) Resposta adequada
- B) Hipoperfusão iatrogênica
- C) Erro de registro
- D) Melhora cardíaca
- E) Hipotermia
**Resposta correta:** B. Sinais de hipoperfusão exigem redução imediata da remoção e reavaliação.

---

## Afirmativas verdadeiro/falso (interativas)

> Confira com `python -m exercicios.modulo_09_balanco_hidrico`.

1. Fração de sobrecarga >10% está associada a maior mortalidade. — **Verdadeiro.** Estudos correlacionam FO elevada a piores desfechos.
2. Peso diário é dispensável quando há ultrassom. — **Falso.** Peso fornece dado objetivo adicional.
3. Bioimpedância ajuda a estimar excesso de fluido intravascular. — **Verdadeiro.** Quantifica fluido total/intravascular.
4. IVC colabada sugere sobrecarga hídrica. — **Falso.** Colapso indica hipovolemia; sobrecarga cursa com IVC dilatada.
5. Ultrafiltração intermitente é sempre superior à contínua. — **Falso.** Escolha depende da estabilidade hemodinâmica.
6. Controle de sódio é irrelevante durante remoção agressiva. — **Falso.** Alterações rápidas podem causar complicações neurológicas.
7. Balanço positivo crônico aumenta tempo de ventilação mecânica. — **Verdadeiro.** Contribui para edema pulmonar.
8. Score VEXUS avalia apenas veia cava inferior. — **Falso.** Inclui doppler hepático, portal e intrarrenal.
9. Metas de balanço devem ser alinhadas com nefrologia diariamente. — **Verdadeiro.** Coordenação multiprofissional é essencial.
10. Lactato normal garante ausência de hipoperfusão. — **Falso.** Deve ser correlacionado com outros parâmetros.
11. Diurético sequencial pode causar alcalose metabólica. — **Verdadeiro.** Perdas de cloro favorecem alcalose.
12. Checklist diário deve incluir plano de reposição eletrolítica. — **Verdadeiro.** Reposições planejadas evitam arritmias.
13. Ultrafiltração deve ser mantida mesmo com hipotensão persistente. — **Falso.** Hipotensão exige ajuste imediato.
14. Ganhos de peso rápidos indicam sobrecarga mesmo sem edema visível. — **Verdadeiro.** Aumento >1 kg/dia sugere acúmulo de fluido.
15. Anotações eletrônicas são suficientes; não é preciso validação da enfermagem. — **Falso.** Dupla checagem reduz erros de registro.
