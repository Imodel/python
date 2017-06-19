from  __future__ import absolute_import,unicode_literals
import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE','DjangoTest.settings')

app = Celery('DjangoTest')

app.config_from_object('django.conf:settings',namespace='CELERY')

app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender,**kwargs):
    sender.add_periodic_task(
        crontab(minute='*/2'),
        test.s("happy crontab"),
    )


'''

app.conf.beat_schedule ={
    'add-ver':{
        'task':'demoapp.tasks.add',
        'schedule':crontab(minute='*/1'),
        'args':(16,16)
    },
}
'''
app.conf.timezone ='UTC'

@app.task
def test(arg):
    print(arg)

@app.task(bind=True)
def debug_task(self):
    print('Request:{0!r}'.format(self.request))