# Simulador — Módulo 15 — Delirium em UTI

Avalie risco, monitore QTc e acompanhe adesão ao bundle.

```python
from simuladores.modulo_15_delirium_uti import cam_icu_result, escore_risco, classificar_risco

positivo = cam_icu_result(True, True, False, True)
escore = escore_risco(35, [5, 10])
print(positivo)
print(classificar_risco(escore))
```

Combine com indicadores institucionais para priorizar pacientes de alto risco e planejar intervenções ambientais e farmacológicas.
