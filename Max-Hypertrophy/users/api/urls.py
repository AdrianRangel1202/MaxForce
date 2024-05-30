from django.contrib import admin
from django.urls import path
from .views import UsersViews, update_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users', UsersViews),
    path('user/', update_user)
]
