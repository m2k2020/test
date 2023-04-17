from django.urls import path
from app import views


urlpatterns = [
    path('', views.index, name='index'),

    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('forgot/', views.forgot, name='forgot'),
    path('staffs/', views.staffs, name='staffs'),


    #region Environment

    path('house/', views.house, name='house'), 
    path('Renter/', views.renter, name='Renter'),
    path('Enviroment/', views.enviroment, name='Enviroment'),

    #endregion





    path('cleaning/', views.cleaning, name='cleaning'),
    
    path('reports/', views.reports, name='reports'),
    path('Payment_Method/', views.Payment_Method, name='Payment_Method'),
    path('Transaction/', views.Transaction, name='Transaction'),
    path('Reports2/', views.Reports2, name='Reports2'),
]