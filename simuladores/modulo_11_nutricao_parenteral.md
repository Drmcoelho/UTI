# Simulador — Módulo 11 — Nutrição Parenteral Total

Utilize `simuladores/modulo_11_nutricao_parenteral.py` para calcular peso ajustado, macros e monitorizar risco de refeeding.

## Exemplos

```python
from simuladores.modulo_11_nutricao_parenteral import ComposicaoNPT, calcular_osmolaridade, avaliar_refeeding

npt = ComposicaoNPT(peso_atual=64, altura_m=1.72, imc_atual=21.6, imc_alvo=22.0, kcal_por_kg=30, proteina_por_kg=1.8)
print(npt.peso_ajustado)
print(npt.calorias_totais)
print(calcular_osmolaridade(600, 1100, 150, outros=100))
print(avaliar_refeeding(fosforo=2.1, magnesio=1.7, potassio=3.3))
```

## Cenários sugeridos
- Ajuste de lipídio diante de triglicerídeos elevados.
- Ritmo de infusão para metas em 16h vs 24h.
- Comparação entre IMC atuais e alvo para recalcular dose proteica.
