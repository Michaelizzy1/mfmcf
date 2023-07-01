from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all-members/', views.members, name='all-members'),
    path('<int:id>/', views.profile, name='profile'),
]