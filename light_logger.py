import json
from datetime import datetime
from pathlib import Path    

date_stamp = f'{datetime.now():%Y-%m}'
logfiles_path = Path.home().joinpath('Marc-perso/Code/logfiles')

if not logfiles_path.exists():
    Path.mkdir(logfiles_path)
logfile_name = f'{date_stamp}_capt02.log'    
logfile = logfiles_path.joinpath(logfile_name)

capt_value = 'dark'

with open('data.txt') as json_file:
    data = json.load(json_file)
if data['light_mode'] == 'dark':
    if capt_value == 'dark':
        pass
    else:
        time_stamp = datetime.now()
        data['light_mode'] = 'light'
        data['time_stamp'] = f'{time_stamp:%Y-%m-%d %H:%M:%S}'
        log_data = f"{time_stamp:%Y-%m-%d %H:%M:%S}_room passed to {data['light_mode']}\n"
        with open(logfile,'a') as f:
            f.write(log_data)
        with open ('data.txt', 'w') as outfile:
            json.dump(data,outfile)
if data['light_mode'] == 'light':
    if capt_value == 'dark':
         time_stamp = datetime.now()
         data['light_mode'] = 'dark'
         data['time_stamp'] = f'{time_stamp:%Y-%m-%d %H:%M:%S}'
         log_data = f"{time_stamp:%Y-%m-%d %H:%M:%S}_room passed to {data['light_mode']}\n"
         with open(logfile,'a') as f:
             f.write(log_data)
         with open ('data.txt', 'w') as outfile:
             json.dump(data,outfile)

print(f"{data['light_mode']}")
