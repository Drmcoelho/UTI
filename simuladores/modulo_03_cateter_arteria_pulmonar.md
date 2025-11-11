# Simulador — Módulo 03

O script [`modulo_03_cateter_arteria_pulmonar.py`](./modulo_03_cateter_arteria_pulmonar.py) calcula resistências vasculares, índice cardíaco e classifica o fenótipo hemodinâmico com base nos dados do cateter de artéria pulmonar.

```bash
python - <<'PY'
from simuladores.modulo_03_cateter_arteria_pulmonar import Hemodinamica, classificar_fenotipo, pronta_retirada

hemo = Hemodinamica(pad_mmHg=18, pap_media_mmHg=31, pcp_mmHg=28, debito_cardiaco_l_min=3.0, superficie_corporea_m2=1.9)
print("IC:", hemo.indice_cardiaco)
print("RVS:", hemo.resistencia_vascular_sistemica(63))
print("Fenótipo:", classificar_fenotipo(hemo))
print("Pronto para retirar CAP?", pronta_retirada(hemo, pam=68, svo2=0.66, lactato=1.8))
PY
```

Os limiares utilizados são provenientes de [`recursos/03_cateter_arteria_pulmonar/parametros_referencia.json`](../recursos/03_cateter_arteria_pulmonar/parametros_referencia.json) para manter coerência com os recursos de bolso.
