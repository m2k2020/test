from django.urls import path
from django.contrib import admin
from app import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('update/<id>/', views.update, name='update'),
#     path('<int:id>/delete/', views.delete, name='delete'),
#     # path('add_class', views.add_class, name='add_class'),
# ]


urlpatterns = [
    path('', views.index, name='index'),
    path('create/',views.create, name='create'),
    path('read/',views.read, name='read'),
    path('edit/<id>',views.edit, name='edit'),
    path('edit/update/<id>',views.update, name='update'),
    path('delete/<id>',views.delete, name='delete'),
    path('fetch_data/',views.fetch_data, name='fetch_data'),



    path('student', views.student, name='student'),
    path('createStudent/',views.createStudent, name='createStudent'),
    path('readStudent/',views.readStudent, name='readStudent'),
]