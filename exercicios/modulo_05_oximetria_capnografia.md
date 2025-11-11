# Exercícios — Módulo 05 — Oximetria e Capnografia

## Como usar

1. Revise o material teórico em `docs/modulo_05_oximetria_capnografia.md` e os casos clínicos correspondentes.
2. Execute o notebook interativo e explore os simuladores associados ao módulo 05.
3. Rode o quiz interativo com `python -m exercicios.modulo_05_oximetria_capnografia` para treinar MCQ e V/F com pontuação em tempo real.
4. Utilize as questões dissertativas como base para discussões em grupo e portfólios reflexivos.

---

## Questões dissertativas

1. **Configuração de monitores de oximetria em pacientes críticos**
   - (a) Quais parâmetros precisam ser configurados ao iniciar monitorização de SpO₂?
   - (b) Como escolher local de sensor considerando perfusão periférica?
   - (c) Quais estratégias minimizam alarmes falsos sem comprometer segurança?
   > 💡 *Gabarito orientador:* Definir alarmes de SpO₂ (alta 98-100%, baixa 92-94% ou personalizadas), ativar índice de perfusão e curva de pletismografia. Selecionar dedos aquecidos, lóbulo da orelha ou frente plantar conforme perfusão; aquecer membros e remover esmalte. Utilizar alarmes escalonados, delays curtos (10-15 s) e revisão diária das metas conforme perfil respiratório.

2. **Integração da capnografia ao manejo ventilatório**
   - (a) Como posicionar sensores mainstream versus sidestream?
   - (b) Quais ajustes devem ser realizados ao detectar diferença elevada entre ETCO₂ e PaCO₂?
   - (c) Quando a capnografia auxilia no diagnóstico de eventos críticos?
   > 💡 *Gabarito orientador:* Mainstream entre tubo e circuito; sidestream próximo à via aérea com linha seca e filtros. Diferença ETCO₂-PaCO₂ > 10 mmHg requer investigar espaço morto, débito cardíaco e calibrar ventilador. Capnografia identifica desconexão, PCR, hipoventilação e retorno espontâneo de circulação.

3. **Análise avançada da curva capnográfica**
   - (a) Como interpretar as fases I-IV da curva?
   - (b) Quais padrões caracterizam broncoespasmo e reinalação?
   - (c) Que parâmetros adicionais devem ser registrados no prontuário?
   > 💡 *Gabarito orientador:* Fase I (inspiração), II (mistura), III (platô alveolar), IV (inspiração). Broncoespasmo gera subida em 'tubarão', reinalação evidencia platô elevado sem retorno à linha de base. Registrar ETCO₂, forma da curva, gradiente com PaCO₂, intervenções realizadas e resposta observada.

---

## Questões de múltipla escolha (interativas)

> Execute `python -m exercicios.modulo_05_oximetria_capnografia` e registre sua pontuação.

### Questão 1 — Qual diferença máxima aceitável entre ETCO₂ e PaCO₂ em ventilação mecânica estável?
- A) 2 mmHg
- B) 5 mmHg
- C) 10 mmHg
- D) 15 mmHg
- E) 20 mmHg
**Resposta correta:** C. Diferença até 10 mmHg é esperada; valores maiores sugerem aumento do espaço morto ou hipoperfusão pulmonar.

### Questão 2 — Platô capnográfico ascendente em dente de tubarão indica
- A) Circuito desconectado
- B) Broncoespasmo
- C) Hiperventilação
- D) Reinalação de CO₂
- E) Fuga no cuff
**Resposta correta:** B. Formato em dente de tubarão é típico de broncoespasmo, sugerindo aumento da resistência expiratória.

### Questão 3 — Índice de perfusão (PI) persistentemente < 0,5% sinaliza
- A) Perfusão periférica adequada
- B) Artefato de movimento
- C) Hipoperfusão periférica grave
- D) Falha do oxímetro
- E) Hipervolemia
**Resposta correta:** C. PI muito baixo indica fluxo capilar insuficiente; deve-se otimizar perfusão e considerar outro sítio para o sensor.

### Questão 4 — Queda súbita para zero na curva de ETCO₂ durante ventilação mecânica indica
- A) Reinalação
- B) Hipotermia
- C) Fuga no cuff
- D) Desconexão ou parada circulatória
- E) Hiperventilação
**Resposta correta:** D. Redução abrupta sugere desconexão, obstrução severa ou PCR; verificar ventilador e checar pulso imediatamente.

### Questão 5 — Qual medida reduz interferência de CO na leitura da SpO₂?
- A) Usar sensor de dedo pediátrico
- B) Aplicar sensor em região com maior melanina
- C) Utilizar oxímetro com tecnologia multiwavelength
- D) Aumentar tempo de integração do sinal
- E) Ajustar alarme de SpO₂ para 85%
**Resposta correta:** C. Oxímetros com múltiplos comprimentos de onda diferenciam carboxihemoglobina da oxihemoglobina, aumentando acurácia.

### Questão 6 — ETCO₂ crescendo progressivamente durante RCP indica
- A) Ventilação excessiva
- B) Compressões eficazes e possível ROSC
- C) Hipotermia
- D) Desconexão do sensor
- E) Erro de calibração
**Resposta correta:** B. Aumento do ETCO₂ durante RCP sugere melhora no fluxo sanguíneo e pode preceder retorno da circulação espontânea.

### Questão 7 — SpO₂ 88% com curva pletismográfica irregular e PI 0,4% significa
- A) Leitura fidedigna; iniciar O₂ suplementar
- B) Artefato por baixa perfusão
- C) Falha de calibragem do monitor
- D) Hiperventilação
- E) Erro de posicionamento arterial
**Resposta correta:** B. PI baixo e curva irregular sugerem artefato; otimizar perfusão e reposicionar sensor antes de intervir agressivamente.

### Questão 8 — Curva de ETCO₂ com retorno incompleto à linha de base sugere
- A) Reinalação de CO₂
- B) Hiperventilação
- C) Hipotermia
- D) Ventilação unipulmonar
- E) Obstrução da cânula nasal
**Resposta correta:** A. Retorno incompleto indica retenção de CO₂ por problemas de circuito ou absorvedor; revisar filtros e válvulas expiratórias.

---

## Afirmativas verdadeiro/falso (interativas)

> Disponível no mesmo script interativo: `python -m exercicios.modulo_05_oximetria_capnografia`.

1. A SpO₂ pode superestimar a saturação arterial em presença de carboxihemoglobina.
   - **Gabarito:** Verdadeiro. Carboxihemoglobina é interpretada como oxihemoglobina pela maioria dos oxímetros convencionais.

2. O valor de ETCO₂ cai rapidamente na embolia pulmonar maciça.
   - **Gabarito:** Verdadeiro. Aumento do espaço morto reduz CO₂ exalado, gerando queda abrupta do ETCO₂.

3. Capnografia sidestream retira grande volume de gás e pode causar hipoventilação.
   - **Gabarito:** Falso. Taxas de amostragem são baixas e não provocam hipoventilação clinicamente significativa.

4. Perfusão periférica preservada garante leitura acurada mesmo com tremores.
   - **Gabarito:** Falso. Movimento causa artefato apesar da boa perfusão; estabilizar o membro é necessário.

5. Capnografia auxilia na confirmação do posicionamento da cânula orotraqueal.
   - **Gabarito:** Verdadeiro. Presença contínua de CO₂ exalado confirma posicionamento traqueal adequado.

6. Índice de perfusão é calculado dividindo a componente pulsátil pela componente estática do sinal.
   - **Gabarito:** Verdadeiro. PI = AC/DC e reflete a amplitude do pulso arterial em relação ao tecido.

7. Temperaturas baixas reduzem a afinidade da hemoglobina pelo oxigênio e elevam a SpO₂.
   - **Gabarito:** Falso. Hipotermia desloca curva para a esquerda (aumenta afinidade), mas pode reduzir perfusão periférica e piorar leitura.

8. Capnograma em forma de 'platô rebaixado' pode indicar ventilação unipulmonar.
   - **Gabarito:** Verdadeiro. Ventilação de um pulmão reduz o volume exalado e altera a fase III, produzindo platô oblíquo baixo.

9. Monitorização contínua de ETCO₂ é recomendada durante sedação procedural profunda.
   - **Gabarito:** Verdadeiro. Capnografia detecta hipoventilação antes de quedas de SpO₂ durante sedação.

10. SpO₂ de 100% exclui hipoxemia em todos os cenários.
   - **Gabarito:** Falso. Em intoxicação por CO ou metemoglobinemia, SpO₂ pode permanecer alta apesar de hipoxemia tecidual.

11. Diferença ETCO₂-PaCO₂ aumenta em pacientes com choque hipovolêmico.
   - **Gabarito:** Verdadeiro. Hipoperfusão aumenta espaço morto fisiológico, ampliando gradiente entre ETCO₂ e PaCO₂.

12. Capnografia nasal não é útil em pacientes em ventilação não invasiva.
   - **Gabarito:** Falso. Interfaces específicas permitem monitorar ETCO₂ e detectar hipoventilação durante VNI.

13. Sinais de reinalação incluem aumento do CO₂ inspiratório (fase I).
   - **Gabarito:** Verdadeiro. Quando há reinalação, a fase inspiratória não retorna a zero e o CO₂ inspirado aumenta.

14. Oxímetros devem ser calibrados manualmente a cada plantão.
   - **Gabarito:** Falso. Dispositivos modernos não exigem calibração manual, apenas testes de funcionalidade periódicos.

15. A monitorização combinada de SpO₂, PI e ETCO₂ fornece panorama da oxigenação, perfusão e ventilação.
   - **Gabarito:** Verdadeiro. Integração dos indicadores permite intervenções precoces baseadas em fisiologia.
