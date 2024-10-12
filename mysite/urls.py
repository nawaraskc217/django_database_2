
from django.contrib import admin
from django.urls import path,include


##main URL
urlpatterns = [
    path('admin/', admin.site.urls),
     path('food/', include('food.urls')), ## food folder->urls, 'food/'-> is url : http://127.0.0.1:8000/food/helloo/ :: /helloo is in urls.py
      path('show/', include('food.urls')),
]
