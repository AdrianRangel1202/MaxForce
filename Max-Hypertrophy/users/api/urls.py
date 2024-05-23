from django.contrib import admin
from django.urls import path
from .views import UsersViews, filter_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', UsersViews),
    path('id=<int:pk>', filter_user)
]
