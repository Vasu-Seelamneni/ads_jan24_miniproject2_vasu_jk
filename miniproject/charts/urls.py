from django.urls import path
from . import views
 
urlpatterns=[
    path('getgraph/',views.Api.getBarGraph, name='get-bar-graph'),
    path('getdata/',views.Api.getData, name='get-data'),
    
]