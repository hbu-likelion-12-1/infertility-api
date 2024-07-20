from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.generate_code, name='generate_code'),
    path('verify/', views.verify_code, name='verify_code'),
]
