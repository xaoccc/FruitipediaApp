from django.urls import path
from fruitipediaApp.profiles import views

urlpatterns = (
    path('create/', views.create, name='profile-create'),
)