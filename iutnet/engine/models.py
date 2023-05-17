from panel.models import Profile
from django.db import models


class Paper(models.Model):
    title = models.CharField(max_length=200, default=None)
    abstract = models.TextField(default=None)
    published_year = models.IntegerField(default=None)
    doi = models.CharField(max_length=300, default=None)

    def __str__(self):
        return self.title

class Dataset(models.Model):
    name            = models.CharField(max_length=25, default=None)
    description     = models.TextField(default=None, blank=True)
    TYPE_CHOICE     = [('EEG','EEG'), ('fMRI','fMRI')]
    type            = models.CharField(choices=TYPE_CHOICE, default='EEG', max_length=10)
    FIELD_CHOICE    = [('MI','Motor Imagery'), ('ERP','ERP')]
    research_field  = models.CharField(choices=FIELD_CHOICE, default='MI', max_length=20)
    data            = models.FileField(upload_to='models/Ai/%Y/%m/%d/', default=None)
    related_paper   = models.ManyToManyField('Paper', blank=True, default=None)
    related_models  = models.ManyToManyField('AiModel', blank=True, default=None)
    private         = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class AiModel(models.Model):
    name            = models.CharField(max_length=25, default='Test-dataset')
    description     = models.TextField(default=None, blank=True)
    Framework_CHOICE= [('Keras','Keras'), ('Pytorch','Pytorch')]
    framework       = models.CharField(choices=Framework_CHOICE, default='Keras', max_length=10)
    Approach_CHOICE = [('DL','Deep Learning'), ('ML','Machine Learning')]
    approach        = models.CharField(choices=Approach_CHOICE, default='ML', max_length=20)
    model           = models.FileField(upload_to='models/Ai/%Y/%m/%d/', default=None)
    related_paper   = models.ManyToManyField('Paper',default=None)
    related_dataset = models.OneToOneField('Dataset', on_delete=models.CASCADE) 
    accuracy        = models.FloatField(default=0.0)
    precision       = models.FloatField(default=0.0)
    recall          = models.FloatField(default=0.0)
    private         = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Request(models.Model):
    user            = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)
    model           = models.OneToOneField('AiModel',on_delete=models.CASCADE)
    dataset         = models.OneToOneField('Dataset', on_delete=models.CASCADE)
    start_time      = models.DateTimeField(auto_now=True)
    end_time        = models.DateTimeField(default=None)

    def __str__(self):
         return self.user.user.username