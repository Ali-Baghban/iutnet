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
    name            = models.CharField(max_length=25, default='Test-dataset')
    description     = models.TextField(default=None, blank=True)
    Framework_CHOICE= [('Keras','Keras'), ('Pytorch','Pytorch')]
    framework       = models.CharField(choices=Framework_CHOICE, default='Keras', max_length=10)
    Approach_CHOICE = [('DL','Deep Learning'), ('ML','Machine Learning')]
    approach        = models.CharField(choices=Approach_CHOICE, default='ML', max_length=20)
    model           = models.FileField(upload_to='models/Ai/%Y/%m/%d/', default=None, blank=True)
    model_code      = models.TextField(default=None, blank=True)
    related_paper   = models.ManyToManyField('Paper',default=None)
    related_dataset = models.OneToOneField('Dataset', on_delete=models.CASCADE) 
    accuracy        = models.FloatField(default=0.0)
    precision       = models.FloatField(default=0.0)
    recall          = models.FloatField(default=0.0)
    private         = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Request(models.Model):

    user            = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True, related_name='demo_request')
    model           = models.OneToOneField('AiModel',on_delete=models.CASCADE)
    dataset         = models.OneToOneField('Dataset', on_delete=models.CASCADE)
    start_time      = models.DateTimeField(auto_now=True)
    end_time        = models.DateTimeField(default=None)

    def __str__(self):
         return self.user.user.username
    
@receiver(post_save, sender=Request)
def dataset_processing(sender, instance, created, **kwargs):
    if created:
        user        = instance.user
        model       = instance.model
        dataset     = instance,dataset
        start_time  = instance.start_time
        opts = {
        'group':'Request processing demo',
        }
        async_task("demoapp.services.request_process", user, model, dataset, start_time, q_options=opts)










class Widget(models.Model):
    name = models.CharField(max_length=140)

