import json
import uvicorn
from fastapi import FastAPI
from config import Config
from config import Raspi
from capteurs_test import Light_captor, Temp_captor

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


@app.get("/api/light")
async def get_light():
    light_capt = Light_captor()
    lum = light_capt.read_state(10)
    donnees = {
        "lum": lum,
    }
    return donnees


@app.get("/api/capteurs")
async def get_capteurs():
    temp_capt = Temp_captor()
    return temp_capt.read_state()

if __name__ == '__main__':
    uvicorn.run("raspi_api:app", port=8000)
