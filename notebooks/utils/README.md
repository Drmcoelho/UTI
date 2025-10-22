# Módulo de Visualização

Este módulo contém funções de visualização reutilizáveis para parâmetros clínicos utilizados nos notebooks educacionais.

## Funções Disponíveis

### `visualizar_parametros_ventilatorios(pbw, vc_alvo, pplat, peep, driving_pressure)`

Cria visualização gráfica dos parâmetros ventilatórios utilizados em ventilação protetora para SDRA.

**Parâmetros:**
- `pbw` (float): Peso Predito (PBW - Predicted Body Weight) em kg
- `vc_alvo` (float): Volume corrente alvo em mL (tipicamente 6 mL/kg PBW)
- `pplat` (float): Pressão de platô em cmH2O
- `peep` (float): PEEP (Positive End-Expiratory Pressure) em cmH2O
- `driving_pressure` (float): Driving pressure (ΔP = Pplat - PEEP) em cmH2O

**Gráficos Gerados:**

1. **Volume Corrente - Ventilação Protetora**
   - Mostra três barras representando:
     - Mínimo aceitável: 4 mL/kg PBW
     - Alvo (destacado em verde): 6 mL/kg PBW
     - Máximo aceitável: 8 mL/kg PBW
   - Linha de referência no valor alvo

2. **Pressões Ventilatórias**
   - Mostra três barras com valores atuais:
     - PEEP (ciano): com linha de referência em 5 cmH2O (mínimo recomendado)
     - Pressão de Platô (vermelho): com linha de referência em 30 cmH2O (máximo recomendado)
     - Driving Pressure/ΔP (amarelo): com linha de referência em 15 cmH2O (limite recomendado)

**Exemplo de Uso:**

```python
from notebooks.utils.visualizacao import visualizar_parametros_ventilatorios

# Parâmetros de um paciente
pbw = 66.0  # kg
vc_alvo = 396.0  # mL (6 mL/kg)
pplat = 28  # cmH2O
peep = 10  # cmH2O
driving_pressure = 18  # cmH2O

# Gerar visualização
visualizar_parametros_ventilatorios(pbw, vc_alvo, pplat, peep, driving_pressure)
```

## Contexto

Esta função foi criada para preservar e modularizar a visualização gráfica que faz parte da `calculadora_ventilacao_protetora` no notebook de SDRA (Síndrome do Desconforto Respiratório Agudo). A visualização ajuda estudantes e profissionais a compreender visualmente se os parâmetros ventilatórios estão dentro das faixas recomendadas para ventilação protetora.

## Referências

- Protocolo ARDSNet para ventilação protetora
- Acute Respiratory Distress Syndrome Network. Ventilation with lower tidal volumes as compared with traditional tidal volumes for acute lung injury and the acute respiratory distress syndrome. N Engl J Med. 2000;342(18):1301-1308.
