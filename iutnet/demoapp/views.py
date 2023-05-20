from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .tasks import add, mul, test_string
from .models import *
# Create your views here.

def test_celery(request):
    #x = add.delay(5,4)
    x = add.delay(5,6)
    y = mul.delay(5,9)
    z = test_string.delay()
    return HttpResponse("We are tring on the process ...")

def dataset_add(request):
    rp = Paper.objects.all()
    if request.method == "POST":
        if 'submit' in request.POST['submit']:
            name            = request.POST['name']
            description     = request.POST['description']
            research_field  = request.POST['research_field']
            data            = request.POST['data_link']
            
            if 'related_paper' in request.POST:
                if 'None' in request.POST['related_paper']:
                    related_paper = None
                else:
                    related_paper   = get_object_or_404(Paper,doi=request.POST['related_paper'])
            else:
                related_paper = None
            
            if 'related_models' in request.POST:
                if 'None' in request.POST['related_models']:
                    related_models = None
                else:
                    related_models   = get_object_or_404(AiModel,name=request.POST['related_models'])
            else:
                related_models = None
            if 'private' in request.POST:
                if 'True' in request.POST['private']:
                    private = True
                else:
                    private = False
            else:
                private = False
            dataset = Dataset.objects.create(name=name, description=description, research_field=research_field, data=data, private=private)
            '''dataset.name            = name
            dataset.description     = description
            dataset.research_field  = research_field
            dataset.data            = data'''
            dataset.related_paper.add(related_paper)
            dataset.related_models.add(related_models)
            '''dataset.private         = private''' 
            return HttpResponse("OK")
        else:
            return HttpResponse("The is some problems ...")
    else:
        context = {'rp': rp}
        return render(request, 'demoapp/dataset.html', context=context)