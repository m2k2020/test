import json
from django.shortcuts import render, redirect
from .forms import AuthorForm
from django.core.files.storage import FileSystemStorage
from .models import Author

# Create your views here.



def author(request):
    # if request.method == 'POST':
    #     form = AuthorForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         print("Save Author")
    # else:
    # form = AuthorForm()

    if request.method == 'POST':
        # name = request.POST.get('name')
        filename = request.FILES.get('file')
        # print(name)
        print(filename)


        fs = FileSystemStorage()
        fname = fs.save(filename.name, filename)
        fapath = fs.path(fname)

        # print(fname)
        # print(fapath)
        # s=""

        files = open(fapath,"r")
        data = json.load(files)

        if data:
            for item in data:
                name = item['name']
                age = item['age']
                adding = Author(name=name,age=age)
                adding.save()
                # print(name,age)
            # Access the keys and values of each dictionary
                # for key, val in item.items():
                #     print(key ,val,"\n")

        else:
            print("No Captured data")

    return render(request, 'author.html')