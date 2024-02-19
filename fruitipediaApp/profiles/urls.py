from django.urls import path
from fruitipediaApp.profiles import views

urlpatterns = (
    path('create/', views.create, name='profile-create'),
    path('details/', views.ProfileDetailView.as_view(), name='profile-details'),
    path('edit/', views.edit, name='profile-edit'),
    path('delete/', views.delete, name='profile-delete'),
)