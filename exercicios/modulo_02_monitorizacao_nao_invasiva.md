# Exercícios — Módulo 02 — Monitorização Hemodinâmica Não Invasiva

## Como usar

1. Revise o material teórico em `docs/modulo_02_monitorizacao_nao_invasiva.md` e os casos clínicos correspondentes.
2. Execute o notebook interativo e explore os simuladores associados ao módulo 02.
3. Rode o quiz interativo com `python -m exercicios.modulo_02_monitorizacao_nao_invasiva` para treinar MCQ e V/F com pontuação em tempo real.
4. Utilize as questões dissertativas como base para discussões em grupo e portfólios reflexivos.

---

## Questões dissertativas

1. **Construção de plano de trending hemodinâmico não invasivo**
   - (a) Quais parâmetros devem ser coletados em série para detecção precoce de deterioração?
   - (b) Como padronizar intervalos de medida e alarmes entre equipe médica e de enfermagem?
   - (c) Quais critérios indicam conversão para monitorização invasiva?
   > 💡 *Gabarito orientador:* Monitorar PAM oscilométrica, FC, índice de perfusão, temperatura periférica e lactato capilar quando disponível. Definir janelas de aferição a cada 15 minutos em instabilidade ou 1 hora em estabilidade, com alarmes de PAM < 65 mmHg e variações > 10 mmHg. Converter para invasiva diante de instabilidade refratária, divergência persistente com dados clínicos, necessidade de vasopressores em titulação rápida ou coleta gasométrica frequente.

2. **Integração da ecocardiografia point-of-care ao monitoramento não invasivo**
   - (a) Como selecionar janelas ecocardiográficas prioritárias para avaliação rápida?
   - (b) Quais medidas permitem estimar débito cardíaco sem cateter invasivo?
   - (c) Como relatar achados críticos de forma estruturada no prontuário?
   > 💡 *Gabarito orientador:* Priorizar eixo paraesternal longo, apical 4 câmaras e subxifoide, avaliando contratilidade global, variação do TSV e colapso de IVC. Estimar débito cardíaco via área do TSV x VTI x FC e integrar com sinais clínicos. Relatar VTI, IVC, presença de derrames e função ventricular com plano de reavaliação em 6-8h.

3. **Segurança e confiabilidade dos dispositivos não invasivos**
   - (a) Quais fatores interferem na leitura de SpO₂ e índice de perfusão?
   - (b) Como validar equipamentos novos antes da adoção ampla na UTI?
   - (c) Que estratégias mitigam alarmes falsos e fadiga de alarmes?
   > 💡 *Gabarito orientador:* Hipotermia, vasoconstrição periférica, pigmentação, esmalte e movimentos artefatuam leituras; aquecer extremidades e reposicionar sensor. Validar equipamentos comparando 10 leituras com padrão ouro e aplicando testes de drift. Configurar alarmes escalonados, utilizar delays inteligentes e revisão diária dos parâmetros para evitar dessensibilização.

---

## Questões de múltipla escolha (interativas)

> Execute `python -m exercicios.modulo_02_monitorizacao_nao_invasiva` e registre sua pontuação.

### Questão 1 — Qual variação máxima aceitável entre três leituras consecutivas de PAM em equipamentos oscilométricos calibrados?
- A) 2 mmHg
- B) 5 mmHg
- C) 8 mmHg
- D) 12 mmHg
- E) 15 mmHg
**Resposta correta:** B. Diferenças acima de 5 mmHg indicam necessidade de repetir medida, reposicionar manguito ou validar com método invasivo.

### Questão 2 — Para garantir leituras acuradas, o manguito deve cobrir qual percentual da circunferência do braço?
- A) 30-40%
- B) 40-50%
- C) 60-80%
- D) 90-100%
- E) 100-120%
**Resposta correta:** C. Manguitos cobrindo 60-80% da circunferência garantem transmissão adequada da pressão; tamanhos menores superestimam valores.

### Questão 3 — Índice de perfusão < 0,7% sugere
- A) Boa perfusão periférica
- B) Artefato sem relevância clínica
- C) Hipoperfusão periférica significativa
- D) Erro de leitura por excesso de luz
- E) Sedação profunda suficiente
**Resposta correta:** C. Valores < 1% apontam hipoperfusão; buscar causas como vasoconstrição, baixo débito ou hipotermia.

### Questão 4 — Qual combinação ecocardiográfica permite estimar volume sistólico sem acesso invasivo?
- A) Diâmetro telediastólico do VE e fração de ejeção
- B) Área da válvula tricúspide e gradiente de pressão
- C) Área do TSV e VTI do TSV
- D) Volume do átrio esquerdo e pressão venosa central
- E) Diâmetro da IVC e saturação venosa central
**Resposta correta:** C. O volume sistólico é obtido multiplicando a área do TSV pelo VTI; multiplicar pelo FC gera o débito cardíaco.

### Questão 5 — Paciente em VNI apresenta discrepância de 15 mmHg entre PAM oscilométrica e sinais clínicos. Próxima etapa?
- A) Assumir leitura e intensificar vasopressor
- B) Solicitar gasometria arterial
- C) Reposicionar manguito e repetir após 5 minutos
- D) Suspender VNI
- E) Iniciar ECMO
**Resposta correta:** C. Discrepância alta requer checar técnica: posicionar manguito corretamente, remover roupas apertadas e repetir medida antes de intervir.

### Questão 6 — Durante monitorização contínua com finger-cuff, queda abrupta do sinal ocorre ao movimentar o braço. Conduta?
- A) Aplicar garrote proximal
- B) Ajustar altura do membro ao nível do coração
- C) Iniciar vasodilatador
- D) Substituir sensor por pulseira pediátrica
- E) Desligar alarmes para evitar ruído
**Resposta correta:** B. Variações hidrostáticas ocorrem com diferença de altura; manter membro ao nível do coração estabiliza leituras.

### Questão 7 — Qual fator mais impacta a confiabilidade da oximetria em pacientes com choque séptico frio?
- A) Uso de antibioticoterapia
- B) Vasoconstrição periférica intensa
- C) Administração de corticoide
- D) Ventilação mecânica
- E) Terapia renal substitutiva
**Resposta correta:** B. Vasoconstrição reduz fluxo capilar e amplitude do sinal, exigindo aquecimento do membro ou troca de sítio (lóbulo da orelha).

### Questão 8 — Qual condição exige escalonamento para linha arterial?
- A) Paciente estável com PAM 72 mmHg
- B) Uso de noradrenalina 0,05 mcg/kg/min sem variações
- C) Divergência recorrente > 10 mmHg e necessidade de titulação rápida de vasopressor
- D) Capnografia final baixa
- E) Paciente agitado durante a aferição
**Resposta correta:** C. Divergência repetida e necessidade de ajustes finos de vasopressor são critérios clássicos para transição à monitorização invasiva.

---

## Afirmativas verdadeiro/falso (interativas)

> Disponível no mesmo script interativo: `python -m exercicios.modulo_02_monitorizacao_nao_invasiva`.

1. Manguito posicionado acima do nível do coração tende a superestimar a pressão arterial.
   - **Gabarito:** Falso. Manguito alto subestima a pressão; se estiver abaixo, ocorre superestimação.

2. Aferições em membros inferiores são aceitáveis quando o membro superior não está acessível.
   - **Gabarito:** Verdadeiro. É possível, porém deve-se ajustar interpretação devido a valores ligeiramente maiores na perna.

3. Oximetria com índice de perfusão > 4% sugere boa perfusão periférica.
   - **Gabarito:** Verdadeiro. Valores elevados indicam fluxo capilar adequado, fortalecendo confiança na leitura de SpO₂.

4. Uso de esmalte escuro altera significativamente a saturação medida.
   - **Gabarito:** Verdadeiro. Pigmentos escuros absorvem luz e podem subestimar a SpO₂; recomenda-se remover esmalte.

5. Diminuição do VTI após manobra de elevação de pernas indica responsividade a fluidos.
   - **Gabarito:** Falso. Aumento do VTI sugere responsividade; queda pode indicar sobrecarga ou disfunção sistólica.

6. Sensores descartáveis tipo adesivo devem ser trocados a cada 24h.
   - **Gabarito:** Verdadeiro. Trocas diárias evitam maceração cutânea e perda de aderência que gera artefato.

7. SpO₂ 92% com gradiente alveolo-arterial normal dispensa investigação adicional.
   - **Gabarito:** Verdadeiro. Se gradiente é adequado e paciente estável, manter observação e correção de fatores reversíveis.

8. Capnografia em circuito fechado não agrega valor à monitorização não invasiva.
   - **Gabarito:** Falso. Capnografia auxilia na avaliação de ventilação, perfusão e detecção precoce de deterioração.

9. Ajustar alarmes de PAM para 50-55 mmHg em choque reduz fadiga de alarmes.
   - **Gabarito:** Falso. Alarmes muito baixos atrasam intervenção e aumentam risco de hipoperfusão irreversível.

10. Monitorização contínua com finger-cuff permite detectar hipotensão ortostática durante mobilização.
   - **Gabarito:** Verdadeiro. Trending beat-to-beat evidencia quedas rápidas de PAM durante mobilização precoce.

11. Ecocardiografia point-of-care substitui necessidade de avaliação cardiológica formal.
   - **Gabarito:** Falso. O POCUS complementa avaliação, mas não substitui estudo completo quando indicado.

12. Variações respiratórias da IVC podem orientar reposição volêmica mesmo sem linha arterial.
   - **Gabarito:** Verdadeiro. Colapso > 50% em ventilação espontânea sugere hipovolemia significativa.

13. Manguitos reutilizáveis devem ser desinfectados apenas quando visivelmente sujos.
   - **Gabarito:** Falso. Recomenda-se limpeza entre pacientes para reduzir infecção cruzada.

14. Índice de perfusão pode prever sucesso de desmame de vasopressores.
   - **Gabarito:** Verdadeiro. Tendência ascendente indica melhora de perfusão periférica e tolerância à redução de drogas.

15. Oscilometria é inútil em fibrilação atrial.
   - **Gabarito:** Falso. Embora haja variabilidade, medir múltiplas vezes e calcular média fornece estimativa confiável.
