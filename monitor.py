
from datetime import datetime
from zoneinfo import ZoneInfo
import json
from pathlib import Path

ZONA = ZoneInfo("America/Santiago")

def ejecutar_monitoreo():
    ahora = datetime.now(ZONA)

    resultado = {
        "fecha_captura": ahora.isoformat(),
        "comparacion": "IKEA vs Falabella",
        "estado": "pendiente_conexion",
        "producto": None,
        "destino": None,
        "promesa_ikea": None,
        "promesa_falabella": None,
        "verificado": False
    }

    carpeta = Path("data")
    carpeta.mkdir(exist_ok=True)

    archivo = carpeta / "ultima_captura.json"

    archivo.write_text(
        json.dumps(
            resultado,
            ensure_ascii=False,
            indent=2
        ),
        encoding="utf-8"
    )

    print("Monitoreo ejecutado:", ahora)
    print("Estado: pendiente de conexión")
    print("Archivo generado:", archivo)

if __name__ == "__main__":
    ejecutar_monitoreo()
