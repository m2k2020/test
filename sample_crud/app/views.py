from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.urls import reverse
from app.models import Class
from .functions import classes


# Create your views here.
def index(request):
    if request.method == "GET":
        listClass = classes.all_classes()
    else:
        savingClass = classes.save_class(request)
        
        if savingClass:            
            return HttpResponseRedirect(reverse('index'))
        else:
            return "error"
        
    context = {'listClass': listClass}
    return render(request, 'index.html',context)

def update(request, id):
    classes = get_object_or_404(Class, id=id)
    data = {
        'id': classes.id,
        'name':classes.name
    }
    print(data)
    return JsonResponse(data)


def delete(request):
    pass