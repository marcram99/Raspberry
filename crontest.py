from crontab import CronTab

my_cron = CronTab(user=True)
rasp = my_cron.find_command('api.py')
for job in rasp:
    print(job)
