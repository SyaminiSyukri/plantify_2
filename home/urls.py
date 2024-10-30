from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.index, name='index'),
    path('<id>/<str:slug>/', views.detail_view, name='details'),
    path('search/', views.search, name='search'),

    path('notes/', views.notes_view, name='notes'),
    path('add_notes/', views.add_notes, name='add_notes'),
   
] 