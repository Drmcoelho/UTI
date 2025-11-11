# Exercícios — Módulo 01 — Monitorização Hemodinâmica Invasiva

## Como usar

1. Revise o material teórico em `docs/modulo_01_monitorizacao_invasiva.md` e os casos clínicos correspondentes.
2. Execute o notebook interativo e explore os simuladores associados ao módulo 01.
3. Rode o quiz interativo com `python -m exercicios.modulo_01_monitorizacao_invasiva` para treinar MCQ e V/F com pontuação em tempo real.
4. Utilize as questões dissertativas como base para discussões em grupo e portfólios reflexivos.

---

## Questões dissertativas

1. **Implantação de PAI em choque séptico refratário**
   - (a) Quais critérios clínicos reforçam a necessidade da linha arterial neste cenário?
   - (b) Como preparar a equipe e o material para garantir assepsia e calibração adequadas?
   - (c) Quais checkpoints imediatos devem ser documentados após a punção?
   > 💡 *Gabarito orientador:* Indicar PAI diante de vasopressores em escalada, necessidade de trending beat-to-beat, lactato elevado e sinais de hipoperfusão periférica. Preparar bandeja estéril, kit pressurizado purgado, checklist de barreira máxima e monitor multiparamétrico calibrado. Documentar sítio de punção, horário, pressões iniciais, teste de Allen, zero atmosférico e parâmetros de alarmes.

2. **Manutenção diária da linha arterial**
   - (a) Quais cuidados reduzem risco de infecção e trombose?
   - (b) Como conduzir a troca do curativo e a avaliação do sítio?
   - (c) Quais indicadores levam à retirada do cateter?
   > 💡 *Gabarito orientador:* Realizar higienização rigorosa, manter sistema pressurizado fechado, evitar desconexões e garantir purge a 3 mL/h. Curativo estéril trocado a cada 7 dias ou quando sujo/úmido, inspeção diária de hiperemia e sinais de isquemia. Retirar após estabilidade hemodinâmica, ausência de necessidade de trending contínuo, queda do risco-benefício ou sinais de infecção.

3. **Integração da monitorização invasiva com a condução da ressuscitação**
   - (a) Como interpretar a curva arterial amortecida versus sobremortecida?
   - (b) Quais parâmetros derivados auxiliam na decisão de fluidos?
   - (c) Como comunicar as metas durante rounds multiprofissionais?
   > 💡 *Gabarito orientador:* Amortecimento sugere bolhas, extensão excessiva ou filtro saturado; sobremortecimento (overshoot) indica tubulação complacente ou pressão dinâmica elevada. Utilizar PAM, PPV, elevação passiva de pernas e testes de oclusão de fim de expiração para orientar fluidos. Registrar metas em prontuário, alinhando PAM alvo, PPV desejada, ajustes de vasopressor e plano de reavaliação com enfermagem e fisioterapia.

---

## Questões de múltipla escolha (interativas)

> Execute `python -m exercicios.modulo_01_monitorizacao_invasiva` e registre sua pontuação.

### Questão 1 — Qual intervalo de tempo é aceitável entre a realização do zero atmosférico e a conexão do sistema ao paciente?
- A) Pode ultrapassar 30 minutos se o circuito permanecer fechado
- B) Até 20 minutos desde que a bolsa permaneça pressurizada
- C) Máximo de 5 minutos para evitar erro por temperatura e bolhas
- D) Zero pode ser feito após a conexão ao paciente sem prejuízo
- E) Não existe recomendação sobre o intervalo
**Resposta correta:** C. Quanto maior o intervalo após o zero, maior a chance de variação térmica e formação de microbolhas; recomenda-se conectar imediatamente (até 5 minutos).

### Questão 2 — Qual estratégia reduz sobremaneira o risco de amortecimento da curva arterial?
- A) Utilizar cateter de polietileno de maior calibre
- B) Aumentar a altura do transdutor acima da linha axilar média
- C) Adicionar filtro bacteriano próximo ao paciente
- D) Manter extensão o mais curta e rígida possível
- E) Injetar 5 mL de ar no flush para aumentar o tônus
**Resposta correta:** D. Tubulação longa/complacente causa amortecimento; usar extensões curtas e rígidas com conexões firmes previne distorção da onda.

### Questão 3 — Paciente com PPV 18% e pressão de pulso 30 mmHg em ventilação controlada. Qual a conduta inicial mais segura?
- A) Iniciar vasopressina em bolus
- B) Avaliar responsividade a fluidos com elevação passiva de pernas
- C) Aumentar a PEEP para 12 cmH₂O
- D) Administrar 500 mL de coloide sem teste prévio
- E) Iniciar nitroprussiato para reduzir pós-carga
**Resposta correta:** B. PPV elevada sugere responsividade a fluidos; teste dinâmico como elevação passiva de pernas evita sobrecarga desnecessária.

### Questão 4 — Ao realizar teste de flush, observa-se retorno oscilatório com mais de três ondas. O que isso indica?
- A) Sistema superdamping, necessitando de filtro adicional
- B) Sistema underdamping com risco de superestimar PAS
- C) Transdutor desalinhado abaixo da linha axilar média
- D) Bolhas de ar no cateter causando artefato
- E) Oclusão arterial iminente
**Resposta correta:** B. Oscilações persistentes após o flush indicam underdamping; é necessário revisar comprimento do tubo e possíveis conexões frouxas para evitar superestimação da PAS.

### Questão 5 — Qual parâmetro integrado à curva arterial sugere necessidade de escalonar vasopressor mesmo com PAM 66 mmHg?
- A) Tempo de enchimento capilar < 2 s
- B) Índice de perfusão periférica 4%
- C) Lactato 5,2 mmol/L e diurese 0,2 mL/kg/h
- D) Saturação venosa central 72%
- E) Temperatura 37,5 ºC
**Resposta correta:** C. PAM marginal com lactato elevado e oligúria indica hipoperfusão; além de otimizar volume, considera-se escalonar vasopressor para metas ≥ 70 mmHg.

### Questão 6 — Durante calibração, a PAM exibida cai para 40 mmHg após desconexão do transdutor da bolsa pressurizada. Qual a causa mais provável?
- A) Buraco no diafragma do transdutor
- B) Bolha residual entre o cateter e o transdutor
- C) Bag pressurizada insuficiente
- D) Falha no sensor de temperatura do monitor
- E) Volume de flush excessivo
**Resposta correta:** C. Quando a bolsa perde pressão (300 mmHg), ocorre refluxo de sangue e queda abrupta da leitura; re-pressurizar imediatamente evita coagulação no sistema.

### Questão 7 — Em paciente com fibrilação atrial, como interpretar PPV de 14%?
- A) Valor confiável para predizer responsividade a fluidos
- B) Necessidade imediata de cateter venoso central
- C) Indicativo de erro de calibração
- D) PPV torna-se menos confiável; combinar com ecocardiografia
- E) Sinal direto para suspender vasopressores
**Resposta correta:** D. Arritmias reduzem a acurácia da PPV; é preciso correlacionar com variação de IVC ou VTI no eco para tomada de decisão.

### Questão 8 — Qual critério abaixo sinaliza retirada segura do cateter arterial?
- A) Noradrenalina 0,3 mcg/kg/min com PAM 68 mmHg
- B) Paciente em ventilação mecânica assisto-controlada
- C) Necessidade de coletas gasométricas a cada 6 horas
- D) Estabilidade hemodinâmica mantida > 24h sem ajustes
- E) Planejamento de cateter venoso central
**Resposta correta:** D. Retirada ocorre quando paciente mantém metas sem ajustes, sem necessidade de trending beat-to-beat ou coletas frequentes, reduzindo risco de infecção e trombose.

---

## Afirmativas verdadeiro/falso (interativas)

> Disponível no mesmo script interativo: `python -m exercicios.modulo_01_monitorizacao_invasiva`.

1. O zero atmosférico deve ser feito com o transdutor aberto ao ar e nivelado na linha axilar média.
   - **Gabarito:** Verdadeiro. Zero incorreto gera erro sistemático de PAM; alinhar à linha axilar evita sub ou superestimação.

2. Flush contínuo acima de 5 mL/h reduz risco de trombose sem efeitos adversos.
   - **Gabarito:** Falso. Taxas elevadas provocam sobrecarga volêmica e risco de hemodiluição; recomenda-se 2-3 mL/h.

3. PPV elevada em ventilação espontânea mantém a mesma interpretação que em ventilação controlada.
   - **Gabarito:** Falso. Respiração espontânea altera ciclos pressóricos; PPV perde acurácia e deve ser evitada.

4. Pressurizar a bolsa em 300 mmHg garante fluxo contínuo e previne refluxo sanguíneo.
   - **Gabarito:** Verdadeiro. 300 mmHg assegura fluxo unidirecional do flush e evita coagulação na linha.

5. A curva arterial sobremortecida (overshoot) tende a subestimar a PAS.
   - **Gabarito:** Falso. Overshoot superestima PAS e subestima PAD; revisar complacência do sistema.

6. Monitorização radial é contraindicada em pacientes com enxerto radial recente.
   - **Gabarito:** Verdadeiro. Uso da artéria radial pode comprometer fluxo do enxerto; preferir sítio alternativo.

7. Ajustar a altura do leito não altera a leitura desde que o transdutor esteja fixo no suporte.
   - **Gabarito:** Falso. Qualquer variação de altura modifica a referência hidrostática; transdutor deve acompanhar o nível do paciente.

8. Curva com incisura dicrótica pouco evidente pode indicar vasoplegia severa.
   - **Gabarito:** Verdadeiro. Vasoplegia reduz resistência vascular e atenua incisura; correlacionar com quadro clínico.

9. Em uso de balão intra-aórtico, a leitura da PAM é inviável.
   - **Gabarito:** Falso. Pode haver artefato, mas PAM média continua mensurável com análise da curva sincronizada.

10. Cateter arterial deve ser trocado rotineiramente a cada 72h para evitar infecção.
   - **Gabarito:** Falso. Trocas programadas aumentam complicações; manter até indicação clínica ou sinais de infecção.

11. Doppler transcraniano pode complementar a monitorização invasiva na avaliação de perfusão.
   - **Gabarito:** Verdadeiro. Fluxo cerebral auxilia na titulação de PAM em pacientes neurocríticos.

12. Amostras para gasometria arterial devem ser coletadas lentamente para evitar colapso da linha.
   - **Gabarito:** Falso. Coletas devem ser firmes e sem refluxo prolongado para minimizar risco de coágulo.

13. Em pacientes com ECMO venoarterial, a curva arterial pode não refletir perfusão coronariana.
   - **Gabarito:** Verdadeiro. Fluxo retrogrado altera forma da onda; interpretar em conjunto com eco e pós-carga.

14. Temperaturas muito baixas no paciente reduzem a viscosidade e melhoram fidelidade da curva.
   - **Gabarito:** Falso. Hipotermia altera resposta do transdutor e aumenta risco de espasmo; curva pode deteriorar.

15. Manter registro diário dos alarmes configurados facilita auditoria de eventos sentinela.
   - **Gabarito:** Verdadeiro. Checklist documentado assegura rastreabilidade e segurança assistencial.
