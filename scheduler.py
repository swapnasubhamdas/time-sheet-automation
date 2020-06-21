from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from time_sheet import time_sheet_reminder

sched = BlockingScheduler()

# Schedule job_function to be called every six hours
sched.add_job(time_sheet_reminder, 'interval', hours = 6)

sched.start()