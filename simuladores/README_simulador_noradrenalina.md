# Simulador Interativo - Titulação de Noradrenalina

Este simulador permite praticar a titulação de noradrenalina em pacientes com choque séptico.

## Como Usar

1. Abra este arquivo em um Jupyter Notebook
2. Execute todas as células
3. Use os controles para ajustar parâmetros
4. Observe as mudanças hemodinâmicas em tempo real

## Requisitos

```python
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider, Dropdown, IntSlider, VBox, HBox, Button, Output
import pandas as pd
```

## Simulador

O código completo está nos notebooks. Este é um exemplo de como os simuladores funcionam:

### Características do Simulador

1. **Parâmetros Ajustáveis:**
   - Dose de noradrenalina (0 - 1.0 mcg/kg/min)
   - Status de volemia (Hipovolemia/Adequada/Hipervolemia)
   - Resistência vascular (Muito Baixa/Baixa/Normal/Alta)
   - Função cardíaca (Reduzida/Normal/Hiperdinâmica)

2. **Monitorização em Tempo Real:**
   - Pressão Arterial Sistólica (PAS)
   - Pressão Arterial Diastólica (PAD)
   - Pressão Arterial Média (PAM)
   - Frequência Cardíaca (FC)
   - Lactato sérico
   - Débito urinário

3. **Feedback Clínico:**
   - Avisos de dose alta
   - Metas atingidas ou não
   - Sugestões de condutas
   - Avaliação de perfusão

### Cenários Disponíveis

#### Cenário 1: Choque Séptico Inicial
- PAM inicial: 55 mmHg
- Lactato: 4.8 mmol/L
- Status: Adequadamente ressuscitado
- Objetivo: Titular noradrenalina para PAM ≥ 65 mmHg

#### Cenário 2: Choque Refratário
- PAM inicial: 60 mmHg
- Lactato: 6.2 mmol/L
- Noradrenalina: 0.3 mcg/kg/min
- Objetivo: Avaliar necessidade de 2ª droga

#### Cenário 3: Disfunção Miocárdica
- PAM inicial: 58 mmHg
- Lactato: 5.5 mmol/L
- Função VE: Reduzida (FE 30%)
- Objetivo: Balancear inotrópico e vasopressor

### Interpretação dos Resultados

**PAM (Pressão Arterial Média):**
- Meta: ≥ 65 mmHg
- Individualizar conforme comorbidades
- Hipertensos: considerar meta de 75-85 mmHg

**Lactato:**
- Normal: < 2 mmol/L
- Elevado: indica hipoperfusão
- Clearance > 10% em 2-4h é bom sinal

**Débito Urinário:**
- Meta: > 0.5 mL/kg/h
- Indicador de perfusão renal

**Dose de Noradrenalina:**
- Baixa: < 0.25 mcg/kg/min
- Moderada: 0.25-0.5 mcg/kg/min
- Alta: > 0.5 mcg/kg/min (considerar 2ª droga)

### Algoritmo de Decisão

```
SE PAM < 65 mmHg:
    SE Noradrenalina < 0.25:
        → Aumentar noradrenalina
    SE Noradrenalina 0.25-0.5:
        → Avaliar volemia
        → SE hipovolemia: bolus
        → SE normovolemia: considerar vasopressina
    SE Noradrenalina > 0.5:
        → Adicionar vasopressina 0.03-0.04 U/min
        → Considerar hidrocortisona 200 mg/dia
        → Reavaliar foco infeccioso

SE PAM ≥ 65 mmHg MAS lactato elevado:
    → Avaliar outras causas de hipoperfusão
    → Considerar função cardíaca
    → Avaliar necessidade de inotrópico
    → Otimizar volemia
```

## Casos Práticos para Treinar

### Caso 1: Sepse Comunitária
Paciente de 65 anos com pneumonia comunitária grave.
- Peso: 70 kg
- Recebeu 30 mL/kg de cristaloide
- PAM inicial: 55 mmHg
- Lactato: 4.8 mmol/L

**Tarefa:** Titular noradrenalina para atingir PAM ≥ 65 mmHg

### Caso 2: Sepse Abdominal
Mulher de 58 anos com peritonite secundária.
- Peso: 65 kg
- PAM: 60 mmHg com noradrenalina 0.4 mcg/kg/min
- Lactato: 6.2 mmol/L (em ascensão)
- Débito: 15 mL/h

**Tarefa:** Identificar choque refratário e adicionar terapias

### Caso 3: Sepse com Disfunção Miocárdica
Homem de 72 anos, ICC prévia (FE 35%), com urosepse.
- Peso: 80 kg
- PAM: 58 mmHg com noradrenalina 0.2 mcg/kg/min
- Lactato: 5.0 mmol/L
- Ecocardiografia: FE 28%, débito baixo

**Tarefa:** Balancear vasoconstrição e suporte inotrópico

## Dicas de Estudo

1. **Primeira Tentativa:**
   - Comece com dose baixa (0.05 mcg/kg/min)
   - Aumente progressivamente
   - Observe resposta da PAM e lactato

2. **Segunda Tentativa:**
   - Experimente diferentes status de volemia
   - Veja como afeta a resposta
   - Compare doses necessárias

3. **Terceira Tentativa:**
   - Teste cenários de choque refratário
   - Pratique identificação de não-responsivos
   - Aprenda quando adicionar 2ª droga

## Conceitos Importantes

### Farmacocinética da Noradrenalina
- **Início:** 1-2 minutos
- **Pico:** 5-10 minutos
- **Duração:** 1-2 minutos após suspensão
- **Meia-vida:** 2-3 minutos

### Efeitos Fisiológicos
- **α1:** Vasoconstrição (↑ RVS → ↑ PAM)
- **β1:** Discreto aumento contratilidade
- **β2:** Mínimo (diferente da adrenalina)

### Armadilhas Comuns

❌ **Erro 1:** Titular muito lentamente
- Paciente permanece hipotenso por muito tempo
- Aumenta lesão de órgãos

❌ **Erro 2:** Usar dose alta sem avaliar volemia
- Pode estar hipovolêmico
- Bolus pode resolver sem drogas altas

❌ **Erro 3:** Não adicionar 2ª droga em choque refratário
- Dose alta de noradrenalina → vasoconstrição excessiva
- Piora perfusão periférica

❌ **Erro 4:** Ignorar disfunção miocárdica
- Noradrenalina aumenta pós-carga
- Pode piorar débito se FE muito baixa

## Referências

1. **Surviving Sepsis Campaign 2021**
   - Noradrenalina como 1ª escolha
   - Meta: PAM ≥ 65 mmHg
   - Vasopressina como 2ª droga

2. **Vincent JL, De Backer D. Circulatory Shock. NEJM 2013**
   - Fisiopatologia do choque
   - Abordagem hemodinâmica

3. **Rhodes A, et al. Surviving Sepsis Campaign Bundles. ICM 2015**
   - Implementação de bundles
   - Desfechos clínicos

## Próximos Passos

Após dominar este simulador:
1. Avance para simulador de bloqueio neuromuscular
2. Pratique ventilação mecânica interativa
3. Teste simulador de ressuscitação volêmica
4. Integre conhecimentos em casos complexos

---

**Execute o notebook completo em `notebooks/` para acessar o simulador interativo!**
