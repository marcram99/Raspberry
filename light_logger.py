import json
from datetime import datetime, timedelta
from pathlib import Path    
from config import Config
import capteurs

logfile = Config.light_logfile
if not logfile.exists():
    logfile.touch()
datafile = Path.cwd().joinpath('data.json')
if not datafile.exists():
    with open(datafile,'w')as new_file:
        json.dump({'light_mode':'dark','change_time':'','mail_time': '', 'mail_alert':0},new_file)
mailwarning_time = timedelta(hours=1)

with open(datafile) as json_file:
    data = json.load(json_file)
    stored_lux = data['light_mode']
    stored_time = data['change_time']
    mail_alert = data['mail_alert']
    mail_time = data['mail_time']
print(25*'-')
print(f"dernière valeur lue: {stored_lux} @ {stored_time}")
capt_value = input('valeur du capeur de lum:')#remplace lecture capt pour test
#capt_value = capteurs.read_lum() 

if stored_lux == 'dark':
    if capt_value == 'dark':
        pass
    if capt_value == 'light':
        time_stamp = datetime.now()
        with open(logfile,'a') as f:
           f.write(f"{time_stamp:%Y-%m-%d %H:%M:%S}_room passed to light\n")
        data = {'light_mode':'light',
                'change_time': f'{time_stamp:%Y-%m-%d %H:%M:%S}',
                'mail_alert': 0}
        with open (datafile, 'w') as json_file:
            json.dump(data, json_file)

if stored_lux == 'light':
    time_stamp = datetime.now()
    first_light = datetime.strptime(stored_time, '%Y-%m-%d %H:%M:%S')
    time_diff = time_stamp - first_light
    if capt_value == 'dark':
        with open(logfile,'a') as f:
           f.write(f"{time_stamp:%Y-%m-%d %H:%M:%S}_room passed to dark\n")
        data = {'light_mode':'dark',
                'change_time': f'{time_stamp:%Y-%m-%d %H:%M:%S}',
                'mail_alert': 0}
        with open (datafile, 'w') as json_file:
            json.dump(data,json_file)
        print(f'la lumière a été allumée pendant: {time_diff}')
    if capt_value == 'light':
        if (time_diff > mailwarning_time) :
            if not mail_alert:
                with open(logfile, 'a') as f:
                    f.write(f"{time_stamp:%Y-%m-%d %H:%M:%S}_mail envoyé pour alarme +1h.\n")
                data = {'light_mode':'light',
                        'change_time': stored_time, 
                        'mail_time':f'{time_stamp:%Y-%m-%d %H:%M:%S}',
                        'mail_alert': 1}
                with open (datafile, 'w') as json_file:
                    json.dump(data, json_file)
                print("lumière allumée depuis plus d'une heure: un mail à été envoyé!")
            if mail_alert:
                last_mail = datetime.strptime(mail_time, '%Y-%m-%d %H:%M:%S')
                time_diff = time_stamp - last_mail
                if time_diff > mailwarning_time:
                    with open(logfile, 'a') as f:
                        f.write(f"{time_stamp:%Y-%m-%d %H:%M:%S}_ nouveau mail envoyé pour alarme +1h.\n")
                    data = {'light_mode':'light',
                            'change_time': stored_time, 
                            'mail_time':f'{time_stamp:%Y-%m-%d %H:%M:%S}',
                            'mail_alert': 1}
                    with open (datafile, 'w') as json_file:
                        json.dump(data, json_file)
