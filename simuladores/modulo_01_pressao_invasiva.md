# Simulador — Módulo 01

Use o script [`modulo_01_pressao_invasiva.py`](./modulo_01_pressao_invasiva.py) para testar cenários de monitorização invasiva.

```bash
python - <<'PY'
from simuladores.modulo_01_pressao_invasiva import calcular_pam, avaliar_ppv, classificar_pam

pas, pad = 95, 55
pam = calcular_pam(pas, pad)
print(f"PAM: {pam:.1f} mmHg")
print(avaliar_ppv(15))
print(classificar_pam(pam))
PY
```

O simulador consulta os dados de referência em [`recursos/01_monitorizacao_invasiva/curvas_referencia.csv`](../recursos/01_monitorizacao_invasiva/curvas_referencia.csv) para oferecer recomendações consistentes com o material de bolso.
