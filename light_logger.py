import json
from datetime import datetime, timedelta
from config import Config
from capteurs_test import Light_captor as capt

now = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
log_file = Config.light_logfile
data_file = Config.data_file
if not data_file.exists():
    with open(data_file, 'w') as new_file:
        json.dump({'light_mode': 'dark',
                   'last_change': now,
                   'warning_level': 0
                   }, new_file)
light_capt = capt()
light_readed = light_capt.read_state(5)

with open(data_file) as json_file:
    data = json.load(json_file)
    light_mode = data["light_mode"]
    last_change = data["last_change"]
    warning_level = data["warning_level"]

print(f'INFO: Data.json = {light_mode} @ {last_change} / {warning_level}')
print(f'INFO: Light value readed: {light_readed}')


def write_2_log(message):
    with open(log_file, 'a') as log:
        log.write(message)


def write_2_json(light, time, level):
    with open(data_file, 'w') as json_file:
        data = {"light_mode": light,
                "last_change": time,
                "warning_level": level
                }
        json.dump(data, json_file)


if light_readed != data['light_mode']:
    last_change = str(datetime.now())
    warning_level = 0
    light_mode = light_readed
    with open(data_file, 'w') as json_file:
        data = {"light_mode": light_readed,
                "last_change": now,
                "warning_level": 0
                }
        json.dump(data, json_file)
    write_2_log(f"{now}_light mode passed to: {light_readed}\n")

else:
    if light_readed == 'light':
        time_delta = datetime.now() - datetime.strptime(last_change, "%Y-%m-%d %H:%M:%S")
        print(f'INFO: time delta = {time_delta}')
        if warning_level < 1:
            if time_delta > timedelta(minutes=5):
                write_2_log(f"{now}_warning level grow to 1\n")
                write_2_json("light", last_change, 1)
        elif warning_level < 2:
            if time_delta > timedelta(minutes=10):
                write_2_log(f"{now}_warning level grow to 2\n")
                write_2_json("light", last_change, 2)

