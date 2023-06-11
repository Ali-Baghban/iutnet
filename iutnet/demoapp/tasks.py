# Create your tasks here

from demoapp.models import Widget
from time import sleep
from celery import shared_task
import subprocess

@shared_task
def add(x, y):
    sleep(5)
    return x + y

@shared_task
def sub_test():
    x = subprocess.run(["python","./scripts/testme.py"], capture_output=True)
    print(x)
    return "Done !!!"

@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def count_widgets():
    return Widget.objects.count()


@shared_task
def rename_widget(widget_id, name):
    w = Widget.objects.get(id=widget_id)
    w.name = name
    w.save()
    
@shared_task
def test_string():
    sleep(10)
    return 'Ali Baghban'