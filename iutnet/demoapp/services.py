#from component.view import downloader, archive
from component.views import downloader,archive, Preprocessor
from datetime import datetime
from time import sleep
import subprocess


def hooker(task):
        print(task.result)
def sleep_and_print(secs):
    sleep(secs)
    path = "XXX"
    print("Task ran!")
    return path

def subprocess_test():
    subprocess.Popen(["python","./scripts/testme.py"])
    print("Task ran!")

def dataset_process(model, dataset_link, name):
    source,_ = downloader.download_file(url=dataset_link, name=name+'.zip')
    path     = 'media/datasets/'+datetime.now().strftime('%Y/%m/%d/%H%M%S/')+name
    archive.unzip(source=source, path=path)
    model.dataset_path = path
    model.ready_to_use = True
    model.save()

def request_process(user, model, dataset, start_time):
    data_path = dataset.dataset_path
    event_id  = [10,11]
    preprocessor = Preprocessor(
        data_path, event_id, montage=False, montage_type="standard_1005",
        filtering=True, l_freq=7.0, h_freq=30.0, events_from="annotations",
        on_missing="warn", tmin=-1.0, tmax=4.0
    )
    preprocessor.runner()
    model.accuracy = 100
    

