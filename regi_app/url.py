from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blockchain', views.blockchain, name='blockchain'),
    path('officerlogin', views.officerlogin, name='officerlogin')
]