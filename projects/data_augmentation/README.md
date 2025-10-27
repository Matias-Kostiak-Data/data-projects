Data augmentation scripts

Este folder contiene un script `augment.py` que genera versiones ampliadas de los CSV en el repositorio.

Requisitos
- Python 3.8+
- Crear y activar un virtualenv en PowerShell

Instalación (PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Uso
```powershell
python augment.py --dir . --out-dir .\augmented --n-multiplier 20
```

Esto leerá los CSV dentro de `Proyecto_1_Ecommerce`, `Proyecto_2_Clima` y `Proyecto_3_Opiniones` (asumiendo la estructura del repo) y escribirá versiones ampliadas en `./augmented`.

Notas
- El script es intencionalmente simple: usa `Faker` para valores sintéticos y preserva columnas y formatos principales.
- Revisa los archivos resultantes y ajusta la semilla/distribuciones según necesites.

Próximos pasos sugeridos
- Añadir control de semilla para reproducibilidad
- Usar `SDV` o técnicas más avanzadas para mantener correlaciones más complejas
- Añadir tests que validen distribuciones y cardinalidades
