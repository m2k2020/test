from django.shortcuts import render,HttpResponse,redirect
from django.http import FileResponse
from django.utils.encoding import smart_str
from app.models import Cases,Files,ZipFile
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your views here.
def index(request):
    return render(request, 'index.html')

def files(request):
    listCases = Cases.objects.all()
    data = {
        'casadata': listCases
    }
    if request.method == 'POST' and request.FILES:
        case = request.POST.get('cases')
        filesFor = request.FILES.getlist('file')
        case_id = Cases.objects.get(id=case)
        # print(case_id)
        for file in filesFor:
            # print(case_id.id,file)
            addFile = Files(file=file , cases=case_id)
            addFile.save()
            if addFile:
                print("Saved All Filkes")
            else:
                print("No Files Added")
        # if isinstance(files, InMemoryUploadedFile):
        #     # handle the file in memory
        #     contents = files.read()
        #     print(contents)
        # print(case," and " , files)
    return render(request, 'files.html',data)

def display_files(request):
    # unique_file = Files.objects.values_list('cases',flat=True)
    # unique = set(unique_file)
    files = Files.objects.all()
    # count = files.distinct('cases')
    data = {
        'files': files
    }
    # for un in unique:
    #     print(un.id)
    # for file in unique_file:
        # print(file.date)
    # if request.method == 'POST':
    #     case = request.POST.get('case')
    #     files = Files.objects.filter(cases=2).all()
    #     # data = {
    #     #         'files': files
    #     # }
    #     return redirect('index')
       

    return render(request, 'display.html',data)

def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        name = uploaded_file.name
        file_contents = uploaded_file.read()
        zip_file = ZipFile(name=name, file=file_contents)
        zip_file.save()
        # return render(request, 'upload_success.html')
        return render(request,"view.html")
    return render(request, 'zipfile.html')

def view_zip(request):
    zipdata = ZipFile.objects.all()
    data = {
        "zipdata": zipdata
    }
    return render(request, 'view.html', data)


def download_zip(request,zip_file_id):
    # if request.method == 'POST':
        # zip_file_id = request.POST.get('id')
         zip_file = ZipFile.objects.get(id=zip_file_id)
         response = HttpResponse(zip_file.file, content_type='application/zip')
         response['Content-Disposition'] = f'attachment; filename="{zip_file.name}"'
         return response
    #     response = HttpResponse(zip_file.file, content_type='application/zip')
    #     response['Content-Disposition'] = f'attachment; filename="{zip_file.name}"'
    # return response