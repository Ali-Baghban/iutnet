from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .tasks import add, mul, test_string, sub_test
from .models import *
# Create your views here.
from django_celery_results.models import TaskResult
from django.http import JsonResponse
from django_q.tasks import async_task

def test_qdjango(request,s):
    json_payload = {
        "message": "hello world!"
    }
    opts = {
        #'task_name':'sleep_and_print',
        'group': 'test_sleep',
            }
    async_task("demoapp.services.sleep_and_print", s, q_options=opts)
    #async_task("demoapp.services.subprocess_test", q_options=opts)

    return JsonResponse(json_payload)

def test_celery(request):
    #x = add.delay(5,4)
    w = sub_test.delay()
    x = add.delay(5,6)
    y = mul.delay(5,9)
    z = test_string.delay()

    return HttpResponse("We are trying on the process ..."+str(x.id))

def celery_result(request):
    
    results = TaskResult.objects.all()
    context = {'results': results}
    return render(request, "demoapp/celery_results.html", context=context)

def paper_add(request):
    if request.method == "POST":
        title           = request.POST.get('title')
        abstract        = request.POST.get('abstract')
        published_year  = request.POST.get('published_year')
        doi             = request.POST.get('doi')
        Paper.objects.create(title=title, abstract=abstract, published_year=published_year, doi=doi)
        return redirect('paper_list')
    else:
        return render(request, 'demoapp/paper_add.html')

def paper_list(request):
    papers = Paper.objects.all()
    context = {'papers' : papers}
    return render(request, 'demoapp/paper_list.html', context=context)

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