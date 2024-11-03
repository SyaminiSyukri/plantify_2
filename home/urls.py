from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.index, name='index'),
    path('<id>/<str:slug>/', views.detail_view, name='details'),
    path('search/', views.search, name='search'),

    path('users/', views.user_list, name='user_list'),  # List all users
    path('users/<int:user_id>/edit/', views.edit_user, name='edit_user'),  # Edit user
    path('users/<int:user_id>/delete/', views.delete_user, name='delete_user'),  #deleting user

    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),
    
    path('notes/', views.notes_view, name='notes'),
    path('add_notes/', views.add_notes, name='add_notes'),
    path('edit_note/', views.edit_note, name='edit_note'),
    path('delete_note/<str:pk>', views.delete_note, name="delete_note")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)