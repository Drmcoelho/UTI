# Exercícios — Módulo 06 — Monitorização da Pressão Intracraniana (PIC)

## Como usar

1. Revise o guia teórico [`docs/modulo_06_pressao_intracraniana.md`](../docs/modulo_06_pressao_intracraniana.md) e execute o notebook dedicado.
2. Simule crises hipertensivas com o material em `simuladores/modulo_06_pressao_intracraniana.py` para praticar cálculos de PPC e escalonamento.
3. Rode o quiz interativo com `python -m exercicios.modulo_06_pressao_intracraniana` para registrar sua pontuação nas MCQ e V/F.
4. Utilize as questões dissertativas para portfólios reflexivos e discussão multiprofissional.

---

## Questões dissertativas

1. **Crise de PIC refratária durante manejo de TCE grave**
   - (a) Quais parâmetros devem ser avaliados imediatamente (PIC, PPC, PRx, PbtO₂)?
   - (b) Como reorganizar o bundle básico antes de iniciar terapias de resgate?
   - (c) Quais critérios definem escalonamento para barbitúrico ou craniectomia descompressiva?
   > 💡 *Gabarito orientador:* Reavaliar PIC, PPC (PAM − PIC), índice de autorregulação (PRx) e PbtO₂ sempre que disponível. Antes de escalar, garantir cabeça a 30°, alinhamento cervical, sedação/analgesia profundas, ventilação controlada (PaCO₂ 35 mmHg) e drenagem de líquor se cateter ventricular. Escalonar quando PIC > 25 mmHg por > 1 hora com PPC < 60 mmHg ou sinais clínicos/imagem de herniação.

2. **Integração da monitorização multimodal**
   - (a) Como correlacionar dados de doppler transcraniano com tendências de PIC?
   - (b) Quais ajustes realizar quando PRx > 0,3 sugerindo perda de autorregulação?
   - (c) Como comunicar achados e decisões durante rounds multiprofissionais?
   > 💡 *Gabarito orientador:* Doppler avalia fluxo médio e índice de pulsatilidade; elevação da IP com PIC alta sugere congestão intracraniana. PRx > 0,3 indica perda de autorregulação — elevar PAM alvo, evitar hipercapnia e considerar osmoterapia. Documentar resumo diário com gráficos PIC/PPC, intervenções e resposta, alinhando metas com neurocirurgia, enfermagem e fisioterapia.

3. **Prevenção de infecção associada ao cateter de PIC**
   - (a) Quais medidas de inserção estéril são mandatórias?
   - (b) Como deve ser o protocolo de manutenção diária?
   - (c) Quando remover o cateter e quais passos seguir após remoção?
   > 💡 *Gabarito orientador:* Aplicar checklist de barreira máxima, antibiótico profilático conforme protocolo e confirmar posicionamento. Manutenção com curativo estéril trocado a cada 72h ou se sujo, manipulação mínima com técnica estéril e monitorização de sódio durante osmoterapia. Remover após controle da PIC ou sinais de infecção; enviar ponta para cultura e documentar vigilância pós-retirada.

---

## Questões de múltipla escolha (interativas)

> Execute `python -m exercicios.modulo_06_pressao_intracraniana` e registre sua pontuação.

### Questão 1 — Paciente com PIC 28 mmHg e PAM 82 mmHg. Qual PPC e conduta imediata?
- A) PPC 54 mmHg; manter conduta
- B) PPC 110 mmHg; reduzir vasopressor
- C) PPC 54 mmHg; otimizar bundle básico
- D) PPC 28 mmHg; iniciar barbitúrico
- E) PPC 82 mmHg; indicar craniectomia
**Resposta correta:** C. PPC = 54 mmHg, abaixo da meta; reforçar medidas básicas antes de terapias de resgate.

### Questão 2 — Qual achado sugere necessidade de drenagem imediata de líquor?
- A) PRx −0,1
- B) PbtO₂ 30 mmHg
- C) Onda B sustentada
- D) PIC oscilando 20-22 mmHg
- E) Onda A (plateau) > 5 min
**Resposta correta:** E. Ondas A prolongadas refletem PIC sustentada alta e baixa complacência.

### Questão 3 — Durante aspiração traqueal, PIC sobe de 20 para 32 mmHg. Estratégia preventiva?
- A) Hiperventilar para PaCO₂ 25 mmHg
- B) Aumentar PEEP para 12 cmH₂O
- C) Bolus prévio de remifentanil e lidocaína
- D) Rebaixar cabeceira para 0°
- E) Administrar furosemida
**Resposta correta:** C. Analgesia e bloqueio simpático minimizam resposta hipertensiva.

### Questão 4 — PRx 0,4 e PPC 50 mmHg. Melhor conduta?
- A) Reduzir PAM alvo para 60 mmHg
- B) Aumentar sedação e reduzir ventilação
- C) Elevar PAM alvo para 90 mmHg
- D) Suspender intervenções
- E) Administrar dexametasona
**Resposta correta:** C. Perda de autorregulação exige elevar PAM alvo para otimizar PPC.

### Questão 5 — Complicação mais associada a cateter intraparenquimatoso?
- A) Hidrocefalia aguda
- B) Infecção ventriculite
- C) Drift de zero e recalibração limitada
- D) Hemorragia intraperitoneal
- E) Hipotensão postural
**Resposta correta:** C. Cateteres parenquimatosos não permitem recalibração após implantação.

### Questão 6 — Alvo de PaCO₂ na ausência de herniação iminente?
- A) 25-30 mmHg
- B) 30-35 mmHg
- C) 35-40 mmHg
- D) 45-50 mmHg
- E) >50 mmHg
**Resposta correta:** C. Manter PaCO₂ 35-40 mmHg evita vasoconstrição cerebral excessiva.

### Questão 7 — Após bolus de solução hipertônica, qual parâmetro monitorar a cada 2-4h?
- A) Amônia sérica
- B) Sódio plasmático
- C) Fibrinogênio
- D) Cálcio iônico
- E) CPK
**Resposta correta:** B. Sódio/osmolaridade devem ser acompanhados de perto para evitar hipernatremia grave.

### Questão 8 — PIC 18 mmHg e PbtO₂ 15 mmHg. Interpretação?
- A) Monitorização normal
- B) Hipoperfusão cerebral apesar da PIC controlada
- C) Erro de calibração
- D) Hiperventilação excessiva
- E) Necessidade imediata de drenagem de líquor
**Resposta correta:** B. PbtO₂ < 20 mmHg indica hipoxia tecidual mesmo com PIC aceitável.

---

## Afirmativas verdadeiro/falso (interativas)

> Disponível no mesmo script interativo: `python -m exercicios.modulo_06_pressao_intracraniana`.

1. PPC é calculada pela diferença entre PAM e PIC. — **Verdadeiro.** PPC = PAM − PIC; meta 60-70 mmHg.
2. Ondas B representam complacência extremamente baixa com risco iminente de herniação. — **Falso.** Ondas B refletem oscilações respiratórias; ondas A (plateau) são mais perigosas.
3. Hiperventilação prolongada para PaCO₂ < 30 mmHg é estratégia segura de longo prazo. — **Falso.** Pode causar isquemia; usar apenas como ponte.
4. PRx negativo sugere autorregulação preservada. — **Verdadeiro.** Correlação inversa PAM/PIC indica autoregulação ativa.
5. Craniectomia descompressiva está indicada quando PIC > 20 mmHg por 5 minutos. — **Falso.** Indicação envolve PIC > 25 mmHg refratária com correlação clínica/radiológica.
6. Monitorização contínua de temperatura e glicemia faz parte do bundle de PIC. — **Verdadeiro.** Hiperglicemia/hipertermia aumentam metabolismo cerebral.
7. Cateter intraventricular permite drenagem terapêutica e calibração periódica. — **Verdadeiro.** Ventriculostomia é padrão-ouro.
8. Uso de bloqueador neuromuscular é contraindicado em PIC elevada. — **Falso.** Pode ser útil para controlar tosse/movimento com monitorização.
9. PbtO₂ < 20 mmHg exige otimização da oxigenação e PPC. — **Verdadeiro.** Meta ≥ 20 mmHg melhora desfechos.
10. Drift do sensor é inexistente em cateteres de fibra óptica. — **Falso.** Há drift progressivo sem recalibração.
11. Avaliar posicionamento do cateter após mobilização reduz leituras falsas. — **Verdadeiro.** Mudanças posturais podem deslocar cateter.
12. Sedação superficial é suficiente para todos os pacientes com PIC elevada. — **Falso.** Frequentemente é necessária sedação profunda.
13. Ondas em dente de serra no doppler transcraniano indicam hiperemia cerebral. — **Falso.** Padrão sugere resistência aumentada.
14. Controle rigoroso de sódio é fundamental durante terapia com salina hipertônica. — **Verdadeiro.** Evita hipernatremia grave e mielinólise.
15. Checklist de PIC deve incluir plano de reavaliação com neurocirurgia. — **Verdadeiro.** Governança multiprofissional reduz variabilidade.
