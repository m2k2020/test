from django.shortcuts import render
from django.http import JsonResponse
from ..models import Class

def book_list(request):
    books = Book.objects.all()
    return JsonResponse({'books': list(books.values())})

def book_create(request):
    title = request.POST.get('title')
    author = request.POST.get('author')
    book = Book.objects.create(title=title, author=author)
    return JsonResponse({'book': model_to_dict(book)})

def book_update(request, pk):
    book = Book.objects.get(pk=pk)
    title = request.POST.get('title')
    author = request.POST.get('author')
    book.title = title
    book.author = author
    book.save()
    return JsonResponse({'book': model_to_dict(book)})

def book_delete(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return JsonResponse({'message': 'Book deleted successfully'})