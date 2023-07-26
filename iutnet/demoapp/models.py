import datetime

from panel.models import Profile
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .services import sleep_and_print
from django_q.tasks import async_task
import shutil
class Paper(models.Model):
    title = models.CharField(max_length=200, default=None)
    abstract = models.TextField(default=None)
    published_year = models.IntegerField(default=None)
    doi = models.CharField(max_length=300, default=None)

    def __str__(self):
        return self.title
@receiver(post_save, sender=Paper)
def create_paper(sender, instance, created, **kwargs):
    if created:
        opts = {
            'group': 'paper_add'
        }
        async_task(sleep_and_print, 5, q_options=opts)

class Dataset(models.Model):
    name            = models.CharField(max_length=25, default=None)
    description     = models.TextField(default=None, blank=True)
    TYPE_CHOICE     = [('EEG','EEG'), ('fMRI','fMRI')]
    type            = models.CharField(choices=TYPE_CHOICE, default='EEG', max_length=10)
    FIELD_CHOICE    = [('MI','Motor Imagery'), ('ERP','ERP')]
    research_field  = models.CharField(choices=FIELD_CHOICE, default='MI', max_length=20)
    dataset_link    = models.URLField(blank=False, null=True, max_length=500)
    dataset_path    = models.CharField(max_length=256, blank=True, null=True)
    related_paper   = models.ManyToManyField('Paper', blank=True, default=None)
    related_models  = models.ManyToManyField('AiModel', blank=True, default=None)
    private         = models.BooleanField(default=False)
    ready_to_use    = models.BooleanField(default=False)

    def __str__(self):
        return self.name
@receiver(post_save, sender=Dataset)
def dataset_processing(sender, instance, created, **kwargs):
    if created:
        dataset_link  = instance.dataset_link
        name          = instance.name
        model         = instance
        opts = {
        'group':'Dataset processing demo',
        }
        async_task("demoapp.services.dataset_process", model, dataset_link, name, q_options=opts)
@receiver(post_delete, sender=Dataset)
def dataset_delete(sender, instance,  **kwargs):
    path = instance.dataset_path
    path = path.split('/')
    path = '/'.join(path[:-1])
    shutil.rmtree(path)

class AiModel(models.Model):
    name            = models.CharField(max_length=25,)
    description     = models.TextField(default=None, blank=True)
    Framework_CHOICE= [('Keras','Keras'), ('Pytorch','Pytorch')]
    framework       = models.CharField(choices=Framework_CHOICE, default='Keras', max_length=10)
    Approach_CHOICE = [('DL','Deep Learning'), ('ML','Machine Learning')]
    approach        = models.CharField(choices=Approach_CHOICE, default='ML', max_length=20)
    model           = models.FileField(upload_to='Ai_models/', default=None, blank=True)
    model_code      = models.TextField(null=True, blank=True)
    related_paper   = models.ManyToManyField('Paper',blank=True)
    related_dataset = models.ManyToManyField('Dataset', blank=True)
    accuracy        = models.FloatField(default=0.0)
    precision       = models.FloatField(default=0.0)
    recall          = models.FloatField(default=0.0)
    results_json    = models.TextField(blank=True)
    private         = models.BooleanField(default=False)

    def __str__(self):
        return self.name
@receiver(post_save, sender=AiModel)
def dataset_processing(sender, instance, created, **kwargs):
    if created:
        if len(instance.model.path) > 0:
            model_file_path = instance.model.path
            ext = model_file_path.split('.')[-1]
            if ext in 'py' or ext in 'PY' :
                with open(model_file_path) as temp:
                    code                = "#This is the first version of the uploaded Ai model that may be updated later\n\n" \
                                          "##################################################################\n\n"
                    code                = code + temp.read()
                    instance.model_code = code
                    instance.save()
class Request(models.Model):

    user            = models.ForeignKey('panel.Profile', on_delete=models.CASCADE,null=True, related_name='demo_request')
    ai_model        = models.ForeignKey('AiModel', on_delete=models.CASCADE, null=True)
    dataset         = models.ForeignKey('Dataset', on_delete=models.CASCADE, null=True)
    test_size       = models.FloatField(max_length=5, default=0.3)
    tmin            = models.FloatField(max_length=5, default=-1)
    tmax            = models.FloatField(max_length=5, default=4)
    event_id        = models.CharField(max_length=30,default="10,11")
    MONTAGE_OPT     = [(False,'None'),('standard_1005','standard_1005'),('standard_1020','standard_1020')]
    montage         = models.BooleanField(default=False)
    montage_type    = models.CharField(choices=MONTAGE_OPT, default='standard_1020', max_length=20)
    FILTER_OPT      = [(False,'None'),('Bandpass', 'Bandpass')]
    filter          = models.CharField(choices=FILTER_OPT, default='Bandpass', max_length=20)
    low_band        = models.FloatField(default=7.0)
    high_band       = models.FloatField(default=30.0)
    EVENT_OPT       = [('annotations','annotations'),('stim','stim')]
    event_from      = models.CharField(max_length=12,choices=EVENT_OPT, default='Annotations')
    MISSING_OPT     = [('Warn', 'warn'), ('x', 'x')]
    on_missing      = models.CharField(max_length=12,choices=MISSING_OPT, default='Warn')
    Stim_Chan       = models.CharField(max_length=100, blank=True)
    EEG_Chan        = models.CharField(max_length=200, blank=True)
    EOG_Chan        = models.CharField(max_length=200, default="'EOG:ch01', 'EOG:ch02', 'EOG:ch03'")
    exclude         = models.CharField(max_length=20, default="bads")
    projection      = models.BooleanField(default=True)
    baseline        = models.CharField(max_length=20, default='None')
    start_time      = models.DateTimeField(default=datetime.datetime.now(), null=True)
    end_time        = models.DateTimeField(null=True, blank=True)
    status          = models.BooleanField(default=False)
    output_shape    = models.CharField(max_length=50, default="(1000,3,250)")
    request_id_hash = models.CharField(max_length=33, blank=True)
    def __str__(self):
         return self.user.user.username
    
@receiver(post_save, sender=Request)
def dataset_processing(sender, instance, created, **kwargs):
    if created:
        instance    = instance
        opts = {
        'group':'Request processing demo v2',
        }
        async_task("demoapp.services.request_process",instance, q_options=opts)
        #async_task("demoapp.services.request_process", instance, q_options=opts)


class Widget(models.Model):
    name = models.CharField(max_length=140)

