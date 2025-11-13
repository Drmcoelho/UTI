# Caso Clínico 01 — Monitorização Hemodinâmica Invasiva em Choque Vasodilatatório

> **Integração curricular:**
> - Notebook principal: [`01_monitorizacao_hemodinamica_invasiva.ipynb`](../notebooks/01_monitorizacao_hemodinamica_invasiva.ipynb)
> - Exercícios: [Bloco 1](../exercicios/exercicios_blocos_1-3.md#-bloco-1-monitorizacao-hemodinamica)
> - Simulador complementar: [`simuladores/modulo_01_pressao_invasiva.py`](../simuladores/modulo_01_pressao_invasiva.py)

## 📋 Apresentação do caso

- **Paciente:** M.A.S., 72 anos, feminina
- **Diagnóstico de base:** hipertensão arterial sistêmica, doença renal crônica estágio 3
- **Motivo da internação:** choque vasodilatatório secundário a sepse urinária, refratário após 30 mL/kg de cristaloide

### Dados iniciais

| Variável | Valor |
| --- | --- |
| Pressão arterial (manguito) | 88/54 mmHg |
| PAM estimada | 65 mmHg |
| FC | 118 bpm |
| Lactato sérico | 4,2 mmol/L |
| Diurese | 0,3 mL/kg/h |
| Temperatura | 38,8 ºC |

O acesso venoso central foi garantido em veia jugular interna direita. O time da UTI discute a necessidade de implantar cateter arterial para monitorização contínua.

## ❓ Perguntas para discussão

### 1. Escolha do sítio arterial

Quais critérios devem direcionar a escolha entre artéria radial e femoral neste cenário?

<details>
<summary>Discussão guiada</summary>

- Radial oferece menor risco de complicações isquêmicas, porém pode falhar em estado de vasoconstrição periférica.
- Avaliar **testes de perfusão**: tempo de enchimento capilar, temperatura da pele, índice de perfusão nos monitores.
- Em choque vasodilatatório com instabilidade, a **artéria femoral** fornece curva mais confiável.
- Checklist antes da punção: avaliar coagulopatia, realizar checklist de barreira máxima e preparar kit pressurizado.
</details>

### 2. Montagem do sistema pressurizado

Liste os passos essenciais para garantir curva arterial fidedigna antes de conectar ao paciente.

<details>
<summary>Discussão guiada</summary>

1. Preparar bolsa pressurizada com SF 0,9% + heparina (2-3 mL/h) e pressurizar a 300 mmHg.
2. Montar o circuito descartável eliminando **todas** as bolhas de ar.
3. Fixar transdutor na linha axilar média (4º espaço intercostal) e realizar zero atmosférico.
4. Executar teste de flush para observar resposta quadrada adequada.
5. Documentar calibração inicial e alarmes configurados no monitor multiparamétrico.
</details>

### 3. Interpretação inicial da curva

Após punção femoral bem-sucedida, os primeiros valores são: PAS 94 mmHg, PAD 52 mmHg, PAM 66 mmHg, com curva discretamente amortecida.

- Qual meta de PAM você mantém para este paciente?
- Como corrigir a amortização observada?

<details>
<summary>Discussão guiada</summary>

- Manter PAM **entre 65-70 mmHg**, ajustando conforme sinais de perfusão.
- Rever posicionamento do membro, procurar bolhas residuais e conferir alinhamento do transdutor.
- Se curva permanecer amortecida, realizar teste de flush e considerar troca de componentes.
</details>

### 4. Reavaliação dinâmica

Duas horas depois, apesar de noradrenalina 0,38 mcg/kg/min, a PAM cai para 62 mmHg e o simulador aponta variação de pressão de pulso (PPV) de 19%.

- Que ferramenta de monitorização invasiva pode auxiliar na decisão de fluidos?
- Quais intervenções imediatas são recomendadas?

<details>
<summary>Discussão guiada</summary>

- Utilizar **elevação passiva de pernas** monitorada pela curva arterial (via PPV) e/ou ecocardiografia focada.
- Executar teste de reposição com 250 mL de cristaloide se houver responsividade dinâmica.
- Preparar adição de vasopressina se PAM permanecer < 65 mmHg após otimização volêmica.
- Registrar efeito de cada intervenção e atualizar alarmes.
</details>

## ✅ Checklist de aprendizado

- [ ] Escolha do sítio arterial baseada em perfusão periférica.
- [ ] Montagem do sistema com eliminação de bolhas e nivelamento adequado.
- [ ] Interpretação da curva com metas de PAM individualizadas.
- [ ] Uso da monitorização para orientar fluidos e escalonamento vasoativo.

> 📌 **Próximo passo:** revise o material de bolso em [`recursos/01_monitorizacao_invasiva/checklist_monitorizacao.md`](../recursos/01_monitorizacao_invasiva/checklist_monitorizacao.md) para padronizar o procedimento com a equipe.
