from django.shortcuts import render
from django.http import HttpResponse
from .tasks import add, mul, test_string

# Create your views here.

def test_celery(request):
    #x = add.delay(5,4)
    x = add.delay(5,6)
    y = mul.delay(5,9)
    z = test_string.delay()
    return HttpResponse("We are tring on the process ...")