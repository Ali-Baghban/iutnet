#from component.view import downloader, archive
from component.views import downloader,archive
from datetime import datetime
from time import sleep
import subprocess
def sleep_and_print(secs):
    sleep(secs)
    print("Task ran!")

def subprocess_test():
    subprocess.Popen(["python","./scripts/testme.py"])
    print("Task ran!")

def dataset_process(dataset_link, name):

    source,_ = downloader.download_file(url=dataset_link, name=name+'.zip')
    path     = 'media/datasets/'+datetime.now().strftime('%Y/%m/%d/%H%M%S/')+name
    archive.unzip(source=source, path=path)


