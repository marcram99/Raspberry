import json
from datetime import datetime, timedelta
from pathlib import Path    

date_stamp = f'{datetime.now():%Y-%m}'
logfiles_path = Path.home().joinpath('Marc-perso/Code/logfiles')
if not logfiles_path.exists():
    Path.mkdir(logfiles_path)
logfile = logfiles_path.joinpath(f'{date_stamp}_capt02.log')
if not logfile.exists():
    with open(logfile, 'w') as f:
        f.write('\n')
datafile = Path.cwd().joinpath('data.txt')
time_mailwarning = timedelta(hours=1)

with open(datafile) as json_file:
    data = json.load(json_file)
    stored_lux = data['light_mode']
    stored_time = data['time_stamp']
print(25*'-')
print(f"dernière valeur lue: {stored_lux} @ {stored_time}")
print(25*'-')

capt_value = input('valeur du capeur de lum:')

if data['light_mode'] == 'dark':
    if capt_value == 'dark':
        pass
    if capt_value == 'light':
        time_stamp = datetime.now()
        data['light_mode'] = 'light'
        data['time_stamp'] = f'{time_stamp:%Y-%m-%d %H:%M:%S}'
        log_data = f"{time_stamp:%Y-%m-%d %H:%M:%S}_room passed to light\n"
        with open(logfile,'a') as f:
            f.write(log_data)
        with open ('data.txt', 'w') as outfile:
            json.dump(data,outfile)
if data['light_mode'] == 'light':
    first_light = datetime.strptime(data['time_stamp'],'%Y-%m-%d %H:%M:%S')
    time_stamp = datetime.now()
    time_diff = time_stamp - first_light
    if capt_value == 'dark':
        print(f'la lumière a été allumée pendant: {time_diff}')
        data['light_mode'] = 'dark'
        data['time_stamp'] = f'{time_stamp:%Y-%m-%d %H:%M:%S}'
        log_data = f"{time_stamp:%Y-%m-%d %H:%M:%S}_room passed to dark\n"
        with open(logfile,'a') as f:
            f.write(log_data)
        with open ('data.txt', 'w') as outfile:
            json.dump(data,outfile)
    if capt_value == 'light':
        print(f' lumière est allumée depuis: {time_diff}')
        if time_diff > time_mailwarning:
            log_data = f"{time_stamp:%Y-%m-%d %H:%M:%S}_mail envoyé pour alarme +1h.\n"
            print("lumière allumée depuis plus d'une heure: un mail à été envoyé!")
            print(f"finish prog with:{data['light_mode']}")
