from datetime import datetime, timedelta
from pathlib import Path

# configuration des différents chemins d'accès des logfiles

class Config():
    files_path = Path.home().joinpath('Raspberry/files')
    logfiles_path = Path.home().joinpath('Raspberry/logfiles')
    if not files_path.exists():
        Path.mkdir(files_path)
    if not logfiles_path.exists():
        Path.mkdir(logfiles_path)
    light_logfile = logfiles_path.joinpath(f'{datetime.now():%Y-%m}_capt02.log')
    temp_logfile = logfiles_path.joinpath(f'{datetime.now():%Y-%m-%d}_capt01.log')
    debug_logfile = logfiles_path.joinpath('00_DEBUG_logfile.log')

    data_file = files_path.joinpath('data.json')
    test_lightcaptor = files_path.joinpath('light.json')
    temp_file = files_path.joinpath('temp.json')

    light_mode = 'dark'
    name = "raspi_hug"
