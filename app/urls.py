from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('add_class', views.add_class, name='add_class'),
]