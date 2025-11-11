# Caso Clínico 02 — Monitorização Hemodinâmica Não Invasiva na UTI Cardíaca

> **Integração curricular:**
> - Notebook principal: [`02_monitorizacao_hemodinamica_nao_invasiva.ipynb`](../notebooks/02_monitorizacao_hemodinamica_nao_invasiva.ipynb)
> - Exercícios: [Bloco 2](../exercicios/exercicios_blocos_1-3.md#-bloco-2-monitorizacao-nao-invasiva)
> - Simulador complementar: [`simuladores/modulo_02_monitorizacao_nao_invasiva.py`](../simuladores/modulo_02_monitorizacao_nao_invasiva.py)

## 📋 Apresentação do caso

- **Paciente:** J.R.N., 65 anos, masculino
- **Diagnóstico de base:** insuficiência cardíaca com fração de ejeção reduzida (30%), fibrilação atrial permanente
- **Motivo da internação:** descompensação cardíaca com hipotensão e hipoperfusão periférica

### Dados iniciais

| Variável | Valor |
| --- | --- |
| PA (manguito automático) | 82/56 mmHg |
| PAM calculada | 65 mmHg |
| Frequência cardíaca | 96 bpm (FA controlada) |
| Saturação periférica | 94% em ar ambiente |
| Índice de perfusão (PI) | 1,2% |
| Temperatura periférica | 35 ºC |

A equipe opta por monitorização **não invasiva** avançada utilizando sistema oscilométrico contínuo com análise de onda de pulso e ecocardiografia à beira leito.

## ❓ Perguntas para discussão

### 1. Escolha da tecnologia

Qual combinação de ferramentas não invasivas fornece melhor avaliação hemodinâmica neste cenário?

<details>
<summary>Discussão guiada</summary>

- Monitorização oscilométrica contínua com cálculo automático de PAM.
- Ecocardiografia point-of-care para estimar VTI do trato de saída do VE.
- Avaliação de índice de perfusão e variação de volume sistólico pelo monitor.
- Capnografia volumétrica pode complementar ao indicar perfusão pulmonar.
</details>

### 2. Validação da pressão arterial

Você realiza três medidas sequenciais com o equipamento oscilométrico:

1. 86/58 mmHg
2. 80/54 mmHg
3. 84/56 mmHg

Calcule a média aritmética e discuta se há necessidade de calibração invasiva.

<details>
<summary>Discussão guiada</summary>

- Média sistólica ≈ (86 + 80 + 84) / 3 = 83,3 mmHg
- Média diastólica ≈ (58 + 54 + 56) / 3 = 56 mmHg
- PAM aproximada: 56 + (83,3 − 56)/3 ≈ 65 mmHg
- Variação < 5 mmHg entre leituras → equipamento confiável; manter método não invasivo.
</details>

### 3. Integração com ecocardiografia

O ecocardiograma focal mostra VTI 14 cm, área de TSV 3,1 cm² e tempo de enchimento mitral restritivo.

- Calcule o débito cardíaco estimado.
- Como ajustar conduta com base no resultado?

<details>
<summary>Discussão guiada</summary>

- Volume sistólico (VS) ≈ VTI × área = 14 × 3,1 ≈ 43,4 mL.
- Débito cardíaco ≈ VS × FC = 43,4 × 96 / 1000 ≈ 4,2 L/min.
- Apesar de PAM limítrofe, DC adequado → priorizar suporte inotrópico leve (dobutamina) + vasodilatadores conforme perfusão.
- Não há indicação imediata de cateter arterial se curva permanece estável.
</details>

### 4. Alarmes e trending

Após 6 horas de suporte, o índice de perfusão sobe para 3,0% e a PAM média se mantém em 68 mmHg.

- Quais parâmetros devem permanecer em trending?
- Como documentar evolução?

<details>
<summary>Discussão guiada</summary>

- Registrar PAM média, variabilidade da FC, índice de perfusão e lactato capilar seriado.
- Utilizar dashboards do monitor e capturas de tela arquivadas em prontuário.
- Repetir ecocardiografia se houver queda abrupta de PI ou saturação venosa central.
</details>

## ✅ Checklist de aprendizado

- [ ] Seleção racional de modalidades não invasivas complementares.
- [ ] Validação da confiabilidade do equipamento oscilométrico.
- [ ] Integração com ecocardiografia à beira leito para estimar débito cardíaco.
- [ ] Documentação estruturada da evolução hemodinâmica.

> 📌 **Próximo passo:** aplique a planilha de trending em [`recursos/02_monitorizacao_nao_invasiva/tabela_trending.csv`](../recursos/02_monitorizacao_nao_invasiva/tabela_trending.csv) para padronizar a reavaliação seriada.
