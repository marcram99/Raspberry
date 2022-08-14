#import capteurs2 as capteurs
import json
from fastapi import FastAPI
from pathlib import Path
from datetime import datetime
from config import Raspi

app = FastAPI()

@app.get("/api")
def api_root():
        return {"welcome to": "Raspi_API"}

@app.get("/api/info")
async def get_info():
        return {"name": Raspi.name,
                "capteur": Raspi.capteur,
                "switch": Raspi.switch,
                }


@app.get("/api/capteurs")
async def get_capteurs():
    temp = capteurs.read_temp()
    hum = capteurs.read_hum()
    lux = capteurs.read_lux()
    ir = capteurs.read_ir()
    lum = capteurs.read_lum(20)

    donnees = {
        "temp": f"{temp:.2f}",
        "hum":f"{hum:.2f}",
        "lux":f"{lux:.2f}",
        "ir":f"{ir:.2f}",
        "lum":lum,
    }
    return donnees
