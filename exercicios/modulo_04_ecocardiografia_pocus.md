# Exercícios — Módulo 04 — Ecocardiografia à Beira do Leito (POCUS)

## Como usar

1. Revise o material teórico em `docs/modulo_04_ecocardiografia_pocus.md` e os casos clínicos correspondentes.
2. Execute o notebook interativo e explore os simuladores associados ao módulo 04.
3. Rode o quiz interativo com `python -m exercicios.modulo_04_ecocardiografia_pocus` para treinar MCQ e V/F com pontuação em tempo real.
4. Utilize as questões dissertativas como base para discussões em grupo e portfólios reflexivos.

---

## Questões dissertativas

1. **Execução do protocolo RUSH em pacientes instáveis**
   - (a) Quais janelas compõem o protocolo e que achados críticos devem ser documentados?
   - (b) Como integrar os achados com sinais vitais e monitorização invasiva/não invasiva?
   - (c) Quais limites definem necessidade de intervenção imediata (ex.: tamponamento)?
   > 💡 *Gabarito orientador:* Protocolo RUSH inclui janelas cardicas (parasternal, apical, subxifoide), pulmonares, cava inferior e vasos pélvicos. Registrar contratilidade global, derrame pericárdico, colapso de IVC, pneumotórax e tamponamento. Integrar com PAM/PPV e estado clínico; tamponamento indicado por derrame com colapso diastólico de VD e IVC tensa requer pericardiocentese.

2. **Quantificação funcional pela ecocardiografia beira-leito**
   - (a) Como estimar fração de ejeção rapidamente?
   - (b) Qual abordagem para medir VTI do TSV e derivar débito cardíaco?
   - (c) Quais parâmetros permitem distinguir choque cardiogênico de distributivo?
   > 💡 *Gabarito orientador:* Utilizar método eyeballing aliado ao Simpson simplificado quando possível, comparando movimento de paredes. Medir diâmetro do TSV em parasternal longo, calcular área (πr²) e multiplicar pelo VTI obtido em apical 5 câmaras; multiplicar por FC para débito. Fração de ejeção baixa com VTI reduzido e RVS elevada sugere choque cardiogênico; FE normal com VTI alto e RVS baixa indica distributivo.

3. **Governança e documentação de estudos à beira-leito**
   - (a) Quais elementos devem constar no laudo resumido?
   - (b) Como arquivar loops e imagens para revisão?
   - (c) Que plano de reavaliação deve ser pactuado com a equipe?
   > 💡 *Gabarito orientador:* Laudo deve conter indicação, janelas obtidas, FE estimada, VTI, IVC, presença de derrames, sinais de congestão pulmonar e recomendações. Loops armazenados no PACS ou pasta segura com identificação do paciente. Planejar reavaliação em 6-12h ou após intervenções (fluido, vasopressor) com checagem cruzada por intensivista ou cardiologista.

---

## Questões de múltipla escolha (interativas)

> Execute `python -m exercicios.modulo_04_ecocardiografia_pocus` e registre sua pontuação.

### Questão 1 — Qual estrutura anatômica deve ser medida para calcular a área do TSV?
- A) Diâmetro interno da válvula mitral
- B) Diâmetro interno do trato de saída do ventrículo esquerdo
- C) Espessura do septo interventricular
- D) Área do átrio esquerdo
- E) Circunferência da válvula tricúspide
**Resposta correta:** B. O diâmetro do TSV (LVOT) em vista paraesternal longo é utilizado para calcular a área e, posteriormente, o volume sistólico.

### Questão 2 — Durante protocolo RUSH, qual achado sugere tamponamento cardíaco?
- A) Hipercinesia global
- B) Derrame pericárdico pequeno sem colapso
- C) Colapso diastólico do ventrículo direito com IVC dilatada
- D) IVC colabando > 50%
- E) Padrão B lines difuso
**Resposta correta:** C. Tamponamento combina derrame relevante, colapso diastólico de VD e IVC distendida sem colapso respiratório.

### Questão 3 — Queda do VTI de 21 para 14 cm após bolus de fluidos indica
- A) Resposta volêmica adequada
- B) Hiperdistensão ventricular
- C) Erro de medição
- D) Necessidade de aumentar vasodilatadores
- E) Tamponamento
**Resposta correta:** B. Redução do VTI após fluidos sugere sobrecarga ou falência ventricular; interromper fluidos e avaliar suporte inotrópico.

### Questão 4 — Qual valor de TAPSE indica disfunção significativa do VD?
- A) > 22 mm
- B) 17-20 mm
- C) < 17 mm
- D) < 25 mm
- E) > 30 mm
**Resposta correta:** C. TAPSE < 17 mm indica disfunção sistólica do ventrículo direito segundo diretrizes da ASE.

### Questão 5 — Em choque distributivo, espera-se encontrar
- A) VE hiperdinâmico com VTI alto
- B) VE hipodinâmico com VTI baixo
- C) Derrame pericárdico volumoso
- D) IVC rígida sem colapso
- E) VD dilatado com septo em D
**Resposta correta:** A. Choque distributivo cursa com hiperdinamismo e VTI elevado; entretanto, avaliar resposta a fluido e tônus vascular.

### Questão 6 — Qual combinação indica congestão pulmonar à ultrassonografia?
- A) Linhas A difusas
- B) Linhas B multifocais bilaterais
- C) Deslizamento pleural preservado
- D) Sinal do código de barras
- E) Sinal do espelho
**Resposta correta:** B. Múltiplas linhas B bilaterais indicam edema intersticial; correlacionar com clínica e PEEP para manejo ventilatório.

### Questão 7 — Ao realizar avaliação de cava inferior em ventilação mecânica controlada, colapso < 12% sugere
- A) Hipovolemia severa
- B) Status volêmico adequado
- C) Sobrecarga volêmica
- D) Erro técnico
- E) Tamponamento
**Resposta correta:** C. Colapso respiratório < 12% em ventilação controlada indica alta pressão de enchimento e possível sobrecarga volêmica.

### Questão 8 — Qual estratégia aumenta a reprodutibilidade da medida de VTI?
- A) Usar amostra maior no Doppler pulsado (PW)
- B) Manter ângulo insonação < 20°
- C) Medir apenas uma vez por exame
- D) Posicionar cursor no centro do átrio esquerdo
- E) Executar manobra de Valsalva
**Resposta correta:** B. Ângulo < 20° minimiza erro de coseno; também promediar 3-5 ciclos melhora consistência entre examinadores.

---

## Afirmativas verdadeiro/falso (interativas)

> Disponível no mesmo script interativo: `python -m exercicios.modulo_04_ecocardiografia_pocus`.

1. POCUS pode ser realizado por intensivistas treinados seguindo protocolos padronizados.
   - **Gabarito:** Verdadeiro. Diretrizes recentes reconhecem competência de intensivistas desde que submetidos a treinamento estruturado.

2. Avaliação de IVC em ventilação espontânea utiliza limiar de colapso > 50% para sugerir hipovolemia.
   - **Gabarito:** Verdadeiro. Colapso acentuado sugere baixa pressão de enchimento em pacientes espontaneamente ventilando.

3. Linhas A indicam edema pulmonar.
   - **Gabarito:** Falso. Linhas A representam pulmão aerado normal; edema gera linhas B.

4. VTI deve ser medido em apical 4 câmaras.
   - **Gabarito:** Falso. O VTI do TSV é medido preferencialmente em apical 5 câmaras alinhando Doppler com fluxo de saída.

5. TAPSE avalia a função sistólica do ventrículo direito.
   - **Gabarito:** Verdadeiro. Tricuspid Annular Plane Systolic Excursion reflete deslocamento longitudinal do VD.

6. Derrame pericárdico pequeno sem colapso exige drenagem imediata.
   - **Gabarito:** Falso. Derrames pequenos sem repercussão podem ser acompanhados clinicamente.

7. Protocolo BLUE diferencia causas de insuficiência respiratória aguda.
   - **Gabarito:** Verdadeiro. BLUE analisa perfis A, B, C para distinguir edema, pneumonia, pneumotórax e tromboembolismo.

8. Ângulo Doppler acima de 60° mantém precisão adequada para VTI.
   - **Gabarito:** Falso. Ângulos altos superestimam VTI; recomenda-se < 20° com correção quando necessário.

9. Choque obstrutivo por TEP pode mostrar VD dilatado e septo em D.
   - **Gabarito:** Verdadeiro. Sobrecarga aguda de pressão no VD causa deformidade septal característica.

10. IVC com diâmetro < 1,5 cm sempre indica hipovolemia.
   - **Gabarito:** Falso. Deve-se considerar contexto clínico; pacientes com PEEP alta podem ter colapso independente de volume.

11. POCUS não substitui ecocardiograma formal quando há suspeita de endocardite.
   - **Gabarito:** Verdadeiro. Casos complexos exigem estudo completo com Doppler e transesofágico se necessário.

12. Sinal do pulmão seco (linhas A e deslizamento presente) descarta pneumotórax.
   - **Gabarito:** Falso. Para descartar pneumotórax é necessário visualizar o sinal do deslizamento ou linhas B; linhas A isoladas não são suficientes.

13. Anotações estruturadas no laudo facilitam auditoria e treinamento.
   - **Gabarito:** Verdadeiro. Templates padronizados garantem rastreabilidade e comparabilidade entre exames.

14. POCUS não deve ser repetido após intervenções para evitar fadiga da equipe.
   - **Gabarito:** Falso. Repetir após terapias permite avaliar resposta e ajustar condutas.

15. Medida de strain global longitudinal é obrigatória em todos os exames beira-leito.
   - **Gabarito:** Falso. Strain é avançado e não obrigatório no POCUS inicial, embora útil quando disponível.
