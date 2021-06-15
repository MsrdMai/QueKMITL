from django.contrib import auth
from django.urls import path,include
from . import views


urlpatterns = [
    path('all_que/', views.all_que, name='all_que'),
    path('type_que/<int:id>/', views.type_que, name='type_que'),
    path('info_type/<int:id>/', views.info_type, name='info_type'),
    path('info/<int:id>/', views.info, name='info'),
    path('booking/<int:id>/', views.booking, name='booking'),
    path('my_booking/<int:id>/', views.my_booking, name='my_booking'),
    
]