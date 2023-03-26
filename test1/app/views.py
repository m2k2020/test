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


def update_view(request, pk):
    if request.method == "GET":
        object = get_object_or_404(Class, pk=pk)
        listClass = classes.all_classes()
        
    # object = get_object_or_404(MyModel, pk=pk)
    # if request.method == 'POST':
    #     form = MyModelForm(request.POST, instance=object)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('myapp:detail', pk=pk)
    # else:
    #     form = MyModelForm(instance=object)
    # return render(request, 'myapp/update_modal.html', {'form': form, 'object': object})

