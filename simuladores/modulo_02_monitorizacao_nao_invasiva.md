# Simulador — Módulo 02

Execute o script [`modulo_02_monitorizacao_nao_invasiva.py`](./modulo_02_monitorizacao_nao_invasiva.py) para validar leituras oscilométricas e estimar débito cardíaco não invasivo.

```bash
python - <<'PY'
from simuladores.modulo_02_monitorizacao_nao_invasiva import (
    carregar_trending,
    validar_serie_pam,
    estimar_debito_cardiaco,
    needs_escalation,
)

leituras = [86, 80, 84]
print("Série válida?", validar_serie_pam(leituras))
print("Débito cardíaco estimado:", estimar_debito_cardiaco(3.1, 14, 96))
print("Necessita escalonar?", needs_escalation(1.2, 65))
print("Trending registrado:")
for entrada in carregar_trending():
    print(entrada)
PY
```
