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
    model_trainer_test()
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

def request_process(instance,user, ai_model, dataset):
    data_path = dataset.dataset_path
    event_id  = [int(item) for item in instance.event_id.split(',')]
    preprocessor = Preprocessor(
        request_id = instance.id,
        data_path=data_path, event_id=event_id, montage=instance.montage, montage_type=instance.montage_type,
        filtering=True, l_freq=instance.low_band, h_freq=instance.high_band, events_from=instance.event_from,
        on_missing=instance.on_missing, tmin=instance.tmin, tmax=instance.tmax
    )
    data = preprocessor.runner()
    instance.output_shape   = data[0].shape
    instance.save()

    '''instance.end_time       = datetime.now()
    instance.status         = True
    ai_model.accuracy       = 85
    ai_model.save()'''

def model_trainer(ai_model=None,option='train'):
    subprocess.Popen(["python","./media/Ai_models/testmodel_1.py"])

def model_trainer_test(ai_model=None,option='train'):
    subprocess.Popen(["python","./media/Ai_models/test.py","Ali","Baghban"])

