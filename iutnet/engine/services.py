from component.views import downloader,archive
from datetime import datetime

def dataset_process(dataset_link, name):

    source,_ = downloader.download_file(url=dataset_link, name=name+'.zip')
    path     = 'media/datasets/'+datetime.now().strftime('%Y/%m/%d/%H%M%S/')+name
    archive.unzip(source=source, path=path)

    