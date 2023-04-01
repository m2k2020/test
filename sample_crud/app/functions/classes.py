from django.shortcuts import render
# from ..models import Class
from app.models import Class
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank, SearchHeadline
from django.core.paginator import Paginator
from django.http import JsonResponse


def all_classes():
    data = Class.objects.all()
    print(data)
    return data


def save_class(request):
    if request.method == 'POST':
        name = request.POST['name']
        classes = Class.objects.create(name=name)

        data = {'class_id': classes.id}

        return JsonResponse(data)



