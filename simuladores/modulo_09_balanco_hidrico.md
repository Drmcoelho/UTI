# Simulador — Módulo 09 — Balanço Hídrico

Script para quantificar sobrecarga, definir metas de remoção e avaliar resposta a diuréticos/ultrafiltração.

```bash
python -i simuladores/modulo_09_balanco_hidrico.py
```

### Exemplo

```python
from simuladores.modulo_09_balanco_hidrico import BalançoHidrico, avaliar_diuretico_sequencial
estado = BalançoHidrico(peso_ideal=68, balanco_acumulado_ml=8000)
print(estado.fracao_sobrecarga)
print(estado.classificar())
print(avaliar_diuretico_sequencial([20, 35, 45]))
```

## Funções

- `BalançoHidrico.fracao_sobrecarga`: calcula % de sobrecarga.
- `calcular_meta_remocao(...)`: taxa de remoção alvo.
- `avaliar_diuretico_sequencial(...)`: classifica resposta.
- `planejar_ultrafiltracao(...)`: recomenda modalidade conforme estabilidade.
