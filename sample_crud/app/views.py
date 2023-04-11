from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.urls import reverse
from app.models import Class
from .functions import classes


# Create your views here.


def index(request):
    return render(request, 'Classes/index.html')
  
def create(request):
    data = Class(name=request.POST['name'])
    data.save()
    return redirect('/')
  
def read(request):
    data = Class.objects.all()
    context = {'data': data}
    return render(request, 'Classes/result.html', context)
  
def edit(request, id):
    data = Class.objects.get(id=id)
    context = {'data': data}
    return render(request, 'Classes/edit.html', context)
  
  
def update(request, id):
    data = Class.objects.get(id=id)
    data.name = request.POST['name']
    data.save()
    return redirect('/')
  
  
def delete(request, id):
    data = Class.objects.get(id=id)
    data.delete()
    return redirect('/')


def fetch_data(request):
    data = Class.objects.values("id","name")
    result=[]
    for row in data:
        result.append(row)
    return JsonResponse(result, safe=False)

























# def index(request):
#     if request.method == "GET":
#         listClass = classes.all_classes()
#     else:
#         savingClass = classes.save_class(request)
        
#         if savingClass:            
#             return HttpResponseRedirect(reverse('index'))
#         else:
#             return "error"
        
#     context = {'listClass': listClass}
#     return render(request, 'index.html',context)

# def update(request, id):
#     classes = get_object_or_404(Class, id=id)
#     data = {
#         'id': classes.id,
#         'name':classes.name
#     }
#     print(data)
#     return JsonResponse(data)


# def delete(request):
#     pass