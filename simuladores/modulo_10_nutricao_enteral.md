# Simulador — Módulo 10 — Nutrição Enteral

Calculadoras para metas calóricas/proteicas, avaliação de tolerância e ajustes de taxa de infusão.

```bash
python -i simuladores/modulo_10_nutricao_enteral.py
```

### Exemplo

```python
from simuladores.modulo_10_nutricao_enteral import PlanoNutricional, cobertura_calorica
plano = PlanoNutricional(peso=76, kcal_kg=30, proteina_kg=1.8, densidade_formula=1.5)
print(plano.volume_alvo)
print(cobertura_calorica(plano, 1600))
```

## Funções

- `PlanoNutricional`: estrutura com metas e volume alvo.
- `cobertura_calorica(...)`: percentual atingido.
- `avaliar_tolerancia(...)`: classifica sinais gastrointestinais.
- `ajustar_taxa_atual(...)`: sugere nova taxa de infusão.
- `necessidade_suplemento_zinco(...)`: avalia suplementação em queimados.
