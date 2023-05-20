from django.urls import path
from .views import test_celery, dataset_add

urlpatterns = [
    path('add', test_celery, name='add-celery'),
    path('dataset', dataset_add, name="dataset_add"),
]
