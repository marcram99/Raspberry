import capteurs
from flask import Flask, render_template, jsonify, request
from pathlib import Path
from datetime import datetime

app = Flask(__name__)

class Vanne():
    def __init__(self):
        self.state = 'off'

    def start(self):
        self.state = 'on'

    def stop(self):
        self.state = 'off'

vanne01 = Vanne()
vanne02 = Vanne()

@app.route('/api/capteur/', methods=['GET'])
def main():
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
        'vanne01': vanne01.state,
        'vanne02': vanne02.state
    }
    return jsonify(donnees) 

@app.route('/api/capteur/', methods=['POST'])
def change_state():
    infos = request.form.to_dict()
    print('request POST')
    if vanne01.state == 'on':
        vanne01.state = 'off'
    else:
        vanne01.state = 'on'
    return {'api_message':'state changed'}
if __name__ == '__main__':
    app.run('0.0.0.0',7000)
