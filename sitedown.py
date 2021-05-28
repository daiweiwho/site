import os, sys
from datetime import datetime
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
import logging

def job_function():
    
    os.system("python sitecopy.py " + '-u' + ' ' + 'https://daily.zhihu.com/')
    os.system("python sitecopy.py " + '-u' + ' ' + 'https://www.baidu.com/')
    os.system("python sitecopy.py " + '-u' + ' ' + 'https://www.hupu.com/')
    os.system("python sitecopy.py " + '-u' + ' ' + 'http://www.gov.cn/')
    os.system("python sitecopy.py " + '-u' + ' ' + 'https://www.jianshu.com/')
    os.system("python sitecopy.py " + '-u' + ' ' + 'https://www.thepaper.cn/')
    os.system("python sitecopy.py " + '-u' + ' ' + 'https://www.bilibili.com/')
    os.system("python sitecopy.py " + '-u' + ' ' + 'https://sspai.com/')
    os.system("python sitecopy.py " + '-u' + ' ' + 'https://www.cnblogs.com/')
    os.system("python sitecopy.py " + '-u' + ' ' + 'https://juejin.cn/')

# 配置日志显示
logging.basicConfig(level=logging.INFO,
                 format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                 datefmt='%Y-%m-%d %H:%M:%S',
                filename='log1.txt',
                filemode='a')



def my_listener(event):
    if event.exception:
        print ('wrong！！！！！！')
    else:
        print ('working...')

scheduler = BlockingScheduler()
scheduler.add_job(job_function, 'interval', hours=1)


# 配置任务执行完成和执行错误的监听
scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

# 设置日志
scheduler._logger = logging

scheduler.start()