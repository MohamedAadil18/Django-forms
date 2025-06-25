from django.contrib import admin
from django.urls import path
from my_form import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', views.register_form),
    path('login', views.login_form)
]
