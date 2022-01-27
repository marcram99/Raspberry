from crontab import CronTab

my_cron = CronTab(user=True)
new = my_cron.new(command='python3 /home/pi/Raspberry/raspi_api.py')
#new.set_comment("job01")
#new.setall('0 * * * *')
#my_cron.remove_all(comment="job01")
new.every_reboot()
my_cron.write()
print('after running:')
rasp = my_cron.find_comment('job01')
for job in rasp:
    print(job)


