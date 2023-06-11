from django.urls import path
from .views import *

urlpatterns = [
    path('test_qdjango/<int:s>', test_qdjango, name="Qdjango"),
    path('add', test_celery, name='add_celery'),
    path('celery', celery_result, name='celery_results'),
    path('dataset', dataset_add, name="dataset_add"),
    path('paper', paper_add, name="paper_add"),
    path('papers', paper_list, name="paper_list"),
]
