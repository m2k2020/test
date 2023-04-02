from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<id>/', views.update, name='update'),
    path('<int:id>/delete/', views.delete, name='delete'),
    # path('add_class', views.add_class, name='add_class'),
]