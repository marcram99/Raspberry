import capteurs
from fastapi import FastAPI
from pathlib import Path
from datetime import datetime

app = FastAPI()

@app.get("/api")
def api_root():
        return {"welcome to": "Raspi_API"}

@app.get("/api/info")
async def get_info():
        return {"name": "raspi cave",
                "capteur": ["temp", "hum", "light", "mov"],
                "switch": ["garage", "voiture", "pompe", "vanne1", "vanne2"]}


@app.get("/api/capteurs")
async def get_capteurs():
    temp = capteurs.read_temp()
    hum = capteurs.read_hum()
    lux = capteurs.read_lux()
    ir = capteurs.read_ir()
    lum = capteurs.read_lum(20)

    donnees = {
        'temp': temp,
        'hum': hum,
        'lux':lux,
        'lum':lum,
        'ir':ir,
    }
    return donnees

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("raspi_api:app", host="0.0.0.0", port=8000, log_level="debug")
    
