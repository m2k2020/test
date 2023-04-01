from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/update/', views.update_view, name='update'),
    # path('add_class', views.add_class, name='add_class'),
]