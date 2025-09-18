from django.urls import path
from . import views
urlpatterns = [
    path('view/', views.viewdata, name='viewdata'),
    path('', views.collectdata, name='collectdata'),
    path('edit/<str:id>/', views.editdata, name='editdata'),
    path('delete/<str:id>/', views.delete, name='delete'),
]
