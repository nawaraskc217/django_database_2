from . import views 
from django.urls import path,include


urlpatterns = [

        path('helloo/',views.index,name='index'),##connects to views.py and index() function ,helloo/: so url is :http://127.0.0.1:8000/food/helloo/
         path('',views.show,name='show') ##connects to views.py and show() function
         
]