from django.urls import path
from .views import test_celery

urlpatterns = [
    path('add', test_celery, name='add-celery'),
]
