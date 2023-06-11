import requests, zipfile, time

class downloader:

    def __init__(self):
        pass

    def download_file(url, name, path='media/datasets_archived/'):
        local_filename = path+name
        start_time = time.time()
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192): 
                    # If you have chunk encoded response uncomment if
                    # and set chunk_size parameter to None.
                    #if chunk: 
                    f.write(chunk)
        finish_time = time.time()
        total_time  = finish_time - start_time
        return local_filename, total_time


class archive:
    def __init__(self):
        pass
    def unzip(source,path='./'):
        with zipfile.ZipFile(source, 'r') as zip_ref:
            zip_ref.extractall(path)
