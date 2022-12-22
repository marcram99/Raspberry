import json
from datetime import datetime
from config import Config

time_stamp = f'{datetime.now():%Y-%m-%d %H:%M:%S}'
debug_logfile = Config.debug_logfile
if not debug_logfile.exists():
    debug_logfile.touch()
logfile = Config.temp_logfile
if not logfile.exists():
    logfile.touch()



class Light_captor():
    def __init__(self):
        self.test_lightcaptor = Config.files_path.joinpath("light.json")
        if not self.test_lightcaptor.exists():
            with open(self.test_lightcaptor, 'w') as json_file:
                json.dump({'light_mode': 'dark'}, json_file)

    def read_state(self, seuil_lum):
        with open(self.test_lightcaptor) as json_file:
            return json.load(json_file)['light_mode']

