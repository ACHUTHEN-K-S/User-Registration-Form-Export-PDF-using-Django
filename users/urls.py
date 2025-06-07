from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.register, name='register'),
    path('pdf/<int:user_id>/', views.generate_pdf, name='generate_pdf'),
]