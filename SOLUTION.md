# Solução: Restauração da Visualização Gráfica na Calculadora de Ventilação Protetora

## Problema Identificado

Durante a refatoração realizada no PR #11, a função `calculadora_ventilacao_protetora` perdeu a visualização gráfica dos parâmetros ventilatórios (Volume Corrente e Pressões). Esses gráficos eram ferramentas visuais importantes para o aprendizado.

## Solução Implementada

A solução restaura a visualização gráfica seguindo o padrão de modularização do PR #11:

### 1. Estrutura Criada

```
notebooks/
└── utils/
    ├── __init__.py
    ├── visualizacao.py  (NOVO)
    └── README.md        (NOVO)

tests/
└── test_visualizacao.py  (NOVO)
```

### 2. Função de Visualização

Criada a função `visualizar_parametros_ventilatorios()` em `notebooks/utils/visualizacao.py`:

- **Parâmetros:**
  - `pbw`: Peso Predito (kg)
  - `vc_alvo`: Volume Corrente alvo (mL)
  - `pplat`: Pressão de Platô (cmH2O)
  - `peep`: PEEP (cmH2O)
  - `driving_pressure`: Driving Pressure/ΔP (cmH2O)

- **Gráficos Gerados:**
  1. **Volume Corrente:** Barras mostrando mínimo (4 mL/kg), alvo (6 mL/kg) e máximo (8 mL/kg)
  2. **Pressões:** Barras para PEEP, Pplat e ΔP com linhas de referência dos limites recomendados

### 3. Integração no Notebook

O notebook `20_sdra.ipynb` foi atualizado:

**Antes (inline):**
```python
def calculadora_ventilacao_protetora(...):
    # ... cálculos ...
    # ... prints ...
    
    # Código inline de ~50 linhas para gráficos
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    # ... código de plotagem ...
    plt.show()
```

**Depois (modular):**
```python
from notebooks.utils.visualizacao import visualizar_parametros_ventilatorios

def calculadora_ventilacao_protetora(...):
    # ... cálculos ...
    # ... prints ...
    
    # Uma linha para gerar os gráficos
    visualizar_parametros_ventilatorios(pbw, vc_alvo, pplat, peep, driving_pressure)
```

### 4. Documentação e Testes

- **README.md**: Documentação completa com exemplos de uso e referências clínicas
- **test_visualizacao.py**: Testes automatizados para garantir funcionamento correto

## Benefícios da Solução

1. ✅ **Preserva a visualização**: Os gráficos educacionais não são perdidos
2. ✅ **Código modular**: Função pode ser reutilizada em outros notebooks
3. ✅ **Manutenção facilitada**: Alterações nos gráficos em um único lugar
4. ✅ **Segue padrão do PR #11**: Consistente com a refatoração proposta
5. ✅ **Testado**: Testes automatizados garantem qualidade
6. ✅ **Documentado**: README explica uso e contexto clínico

## Uso

```python
# No notebook
from notebooks.utils.visualizacao import visualizar_parametros_ventilatorios

# Gerar visualização com parâmetros de um paciente
visualizar_parametros_ventilatorios(
    pbw=66.0,          # Peso predito em kg
    vc_alvo=396.0,     # Volume corrente alvo em mL
    pplat=28,          # Pressão de platô em cmH2O
    peep=10,           # PEEP em cmH2O
    driving_pressure=18 # ΔP em cmH2O
)
```

## Validação

- ✅ Função executa sem erros
- ✅ Gráficos são gerados corretamente
- ✅ Valores são exibidos nas barras
- ✅ Linhas de referência aparecem nos gráficos
- ✅ Testes automatizados passam
- ✅ Código funciona no contexto do notebook

## Conclusão

A visualização gráfica foi restaurada de forma modular, preservando seu valor educacional enquanto melhora a organização do código. A solução está alinhada com os objetivos de refatoração do PR #11 e adiciona valor através de testes e documentação.
