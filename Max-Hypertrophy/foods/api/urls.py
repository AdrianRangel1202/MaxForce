from django.contrib import admin
from django.urls import path
from .views import  FoodViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', FoodViews)
]
