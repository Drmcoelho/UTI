# Simulador — Módulo 07 — Acesso Venoso Central

Ferramentas para avaliar risco infeccioso, cumprimento de bundles e seleção de sítio.

## Uso rápido

```bash
python -i simuladores/modulo_07_acesso_venoso_central.py
```

### Exemplo

```python
from simuladores.modulo_07_acesso_venoso_central import AvaliacaoCVC, avaliar_bundle
estado = AvaliacaoCVC(dias_curativo=5, temperatura=37.8, sinais_locais=False, bundle_insercao=True)
print(estado.risco_infeccao())
print(avaliar_bundle([True, True, False, True]))
```

## Funções

- `AvaliacaoCVC.risco_infeccao()`: síntese de risco atual.
- `dias_para_troca_curativo(dias)`: define prazo de troca.
- `avaliar_bundle(itens)`: calcula percentual do bundle cumprido.
- `necessidade_cultura(...)`: indica coleta imediata.
- `sugestao_via_acesso(...)`: orienta escolha do próximo sítio.
