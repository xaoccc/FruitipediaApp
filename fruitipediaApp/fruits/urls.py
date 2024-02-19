from django.urls import path, include
from fruitipediaApp.fruits import views

urlpatterns = (
    path('', views.HomePageView.as_view(), name='index'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('fruit/', include([
        path('create/', views.FruitCreateView.as_view(), name='create fruit'),
        path('<int:pk>/', include([
            path('details/', views.FruitDetailView.as_view(), name='details fruit'),
            path('edit/', views.FruitEditView.as_view(), name='edit fruit'),
            path('delete/', views.delete_fruit, name='delete fruit'),
            ])),
        ])
    ),
)

