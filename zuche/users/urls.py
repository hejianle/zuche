from django.urls import path
from users import views

urlpatterns = [
    path('kauth/', views.login),
]