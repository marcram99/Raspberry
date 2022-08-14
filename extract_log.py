from pathlib import Path
from datetime import datetime, date, time
from config import Config

logfile_path = Config.logfiles_path

def min_max(my_file):
    temp_tab = []
    time_tab = []
    with my_file.open() as f:
        for line in f.readlines():
            time_stamp, raw_temp, hum = line.split('_')
            dt = datetime.strptime(time_stamp, "%Y-%m-%d %H:%M:%S")
            time = f'{dt.time().hour:02d}:{dt.time().minute:02d}'
            temp = float(raw_temp[2:])
            temp_tab.append(temp)
            time_tab.append(time)
    min_temp = min(zip(temp_tab, time_tab))
    max_temp = max(zip(temp_tab, time_tab))
    return(f'min = {min_temp} / max = {max_temp}')

if __name__ == '__main__':
    #my_file = logfile_path.joinpath(f'2022-08-07_capt01.log')
    #print(min_max(my_file))
    log_list = sorted(logfile_path.glob('*_capt01.log'))
    for line in log_list:
        try:
            print(min_max(line))
        except ValueError:
            print(line)
    
