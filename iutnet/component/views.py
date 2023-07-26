import requests, zipfile, time, mne, glob, hashlib
import subprocess
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

class Preprocessor:
    def __init__(
            self, request_id, data_path,event_id,montage=False,montage_type="standard_1005",
            filtering=True,l_freq=7.0,h_freq=30.0,events_from="annotations",
            on_missing="warn",tmin=-1.0,tmax=4.0
            ):
        self.request_id     = hashlib.md5(str(request_id).encode('utf-8')).hexdigest()
        self.data_path      = data_path
        self.montage        = montage
        self.montage_type   = montage_type
        self.filtering      = filtering
        self.l_freq         = l_freq 
        self.h_freq         = h_freq
        self.events_from    = events_from
        self.event_id       = event_id
        self.on_missing     = on_missing
        self.tmin           = tmin
        self.tmax           = tmax
        self.fname_path     = './media/epochs/'
    
    def create_reader(self):
            dict = {
                'edf': mne.io.read_raw_edf(),
                'gdf': mne.io.read_raw_gdf(),
            }
            return dict
    def read_raw(self,path):
        raw = mne.io.read_raw_gdf(path, eog=['EOG:ch01', 'EOG:ch02', 'EOG:ch03'], preload=True, verbose=False)
        raw.pick_types(meg=False, eeg=True, stim=False, eog=False, exclude="bads")
        return raw

    def data_loader(self):
        path = glob.glob(self.data_path+'/*')
        if len(path) > 0 :
            extention = path[0].split('.')[-1]
            path = glob.glob(self.data_path+"/*."+extention)
        ######################
        # select reader type
        ######################
        raw_array = [self.read_raw(i) for i in path]
        raw = mne.concatenate_raws([i for i in raw_array])
        if self.montage is True:
            montage = mne.channels.make_standard_montage(self.montage_type)
            raw.set_montage(montage)
        if self.filtering is not False:
            # Apply band-pass filter
            raw.filter(l_freq=self.l_freq, h_freq=self.h_freq, fir_design="firwin", skip_by_annotation="edge")
        return raw
    def events_maker(self, raw):
        if self.events_from == 'annotations':
            events = mne.events_from_annotations(raw)
        elif self.events_from == 'stim':
            pass
        return events
    def epochs_maker(self,raw,events):
        picks   = mne.pick_types(raw.info, meg=False, eeg=True, stim=False, eog=False, exclude="bads")
        epochs  = mne.Epochs(
            raw         = raw,
            events      = events[0],
            event_id    = self.event_id,
            tmin        = self.tmin,
            tmax        = self.tmax,
            proj        = True,
            picks       = picks,
            baseline    = None,
            on_missing  = self.on_missing,
            preload     = True,
        )
        labels  = epochs.events[:,-1]

        return epochs, labels
    def epochs_save(self,epochs):
        fname = self.fname_path+self.request_id+'-epo.fif'
        mne.Epochs.save(epochs,fname=fname,split_size='2GB')
    def runner(self):
        raw             = self.data_loader()
        events          = self.events_maker(raw=raw)
        epochs, labels  = self.epochs_maker(raw=raw,events=events)
        data            = epochs.get_data()
        self.epochs_save(epochs=epochs)
        return data, epochs, labels

class ModelTrainer:
    '''def __int__(self, request_id):
        self.request_id = hashlib.md5(str(request_id).encode('utf-8')).hexdigest()
        self.fname_path = './media/epochs/'
        '''

    def get_request_id(self,request_id):
        encoded_request_id = hashlib.md5(str(request_id).encode('utf-8')).hexdigest()
        return encoded_request_id

    def runner(self,model_path,request_id):
        subprocess.Popen(["python", model_path, request_id])


