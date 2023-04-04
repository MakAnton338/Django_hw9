from django.urls import path

from . import views

app_name = 'triangle'
urlpatterns = [
    path('', views.triangle, name='triangle'),
    path('user/', views.person_list, name='person_list'),
    path('person/', views.person_register, name='person_register'),
    path('person/<int:pk>/', views.person_upd, name='person_upd'),
    ]
