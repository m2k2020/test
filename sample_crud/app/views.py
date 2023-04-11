from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.urls import reverse
from app.models import Class,Student
from .functions import classes


# Create your views here.

#region Class
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


#endregion


def student(request):
    return render(request, 'Student/index.html')


def createStudent(request):
    new_name = request.POST['name']
    new_age = request.POST['age']
    new_gradeid = request.POST['grade_id']
    print(new_name + " " + new_age + " " + new_gradeid)

    if new_name is None:
        print("Please enter Name: ")
    if new_age is None:
        print("Please enter Age: ")
    if new_gradeid is None:
        print("Please enter Grade ID: ")

    else:
        id_class = Class.objects.get(id=new_gradeid)
        id=id_class.id
        add_Student = Student(name=new_name, age=new_age, grade_id=id)
        add_Student.save()
        return redirect('/')
    

def readStudent(request):
    students = Student.objects.all()
    context = {'data': students}
    return render(request, 'Student/stresult.html', context)

























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