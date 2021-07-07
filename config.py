from datetime import datetime, timedelta
from pathlib import Path    

class Config():
    logfiles_path = Path.home().joinpath('Documents/Python/logfiles')
    if not logfiles_path.exists():
        Path.mkdir(logfiles_path)

    light_logfile = logfiles_path.joinpath(f'{datetime.now():%Y-%m}_capt02.log')
    temp_logfile = logfiles_path.joinpath(f'{datetime.now():%Y-%m-%}_capt01.log')    
    debug_logfile = logfiles_path.joinpath(f'00_DEBUG_logfile.log')

    seuil_nuit = 40
