from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .tasks import add, mul, test_string, sub_test
from .models import *
# Create your views here.
from django_celery_results.models import TaskResult
from django.http import JsonResponse
from django_q.tasks import async_task, result

def test_qdjango(request,s):
    json_payload = {
        "message": "Good morning dear Dr. Zali ... :)"
    }
    opts = {
        #'task_name':'sleep_and_print',
        
        'group': 'test_sleep',
            }
    
    x = async_task("demoapp.services.sleep_and_print", s, q_options=opts)
    print (result(x,2))
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

import matplotlib.pyplot as plt
import io
import urllib, base64

def create_plot():
    plt.figure()
    x = [2.5166141986846924, 2.4337246417999268, 2.3756425380706787, 2.320280075073242, 2.263989210128784,
              2.204336166381836, 2.139326810836792, 2.064134120941162, 1.9762555360794067, 1.8678804636001587]
    y = [2.4625356197357178, 2.408228635787964, 2.3579623699188232, 2.30776047706604, 2.2547502517700195,
                  2.1977176666259766, 2.1339569091796875, 2.0592479705810547, 1.967551350593567, 1.8528684377670288]
    {"loss": [2.5166141986846924, 2.4337246417999268, 2.3756425380706787, 2.320280075073242, 2.263989210128784,
              2.204336166381836, 2.139326810836792, 2.064134120941162, 1.9762555360794067, 1.8678804636001587],
     "accuracy": [0.0, 0.3660714328289032, 0.7142857313156128, 0.7053571343421936, 0.6785714030265808,
                  0.6071428656578064, 0.5892857313156128, 0.5535714030265808, 0.5, 0.5178571343421936],
     "val_loss": [2.4625356197357178, 2.408228635787964, 2.3579623699188232, 2.30776047706604, 2.2547502517700195,
                  2.1977176666259766, 2.1339569091796875, 2.0592479705810547, 1.967551350593567, 1.8528684377670288],
     "val_accuracy": [0.0416666679084301, 0.4583333432674408, 0.5208333134651184, 0.5416666865348816,
                      0.5208333134651184, 0.5, 0.4791666567325592, 0.5, 0.5, 0.5]}
    plt.title("Model Metrics")
    plt.plot(x, y)

    # Convert plot to PNG image
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())

    uri = urllib.parse.quote(string)
    return uri
def plot_view(request):
    plot = create_plot()
    return render(request, 'demoapp/plot.html', {'plot': plot})
