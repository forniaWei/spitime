import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from common.data import data

def job1():
    print('job1', datetime.datetime.now())

    scheduler = BlockingScheduler()

    # 每两小时执行一次

    scheduler.add_job(data, 'interval', hours=2, id='job1')

    scheduler.start()


