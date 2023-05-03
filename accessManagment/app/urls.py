from django.urls import path
from app import views



urlpatterns = [
    path('', views.index, name='index'),
    path('files/', views.files, name='files'),
    path('Viewfiles/', views.display_files, name='Viewfiles'),

    path('zipfile/', views.upload_file, name='zipfile'),
    path('view/', views.view_zip, name='view'),
    path('downloadFile/<int:zip_file_id>/', views.download_zip, name='downloadFile'),

]