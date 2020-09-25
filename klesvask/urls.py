from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='klesvask'),
    path('reg_vask/', views.regWash, name='reg_vask'),
    path('queue/', views.addToQueue, name='queue'),
]