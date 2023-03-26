from django.shortcuts import render
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




