from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='home'),
    path('users/', views.users, name='users'),
    path('groups/', views.groups, name='groups'),
    path('adduser/', views.adduser, name='adduser'),
    path('addgroup/', views.addgroup, name='addgroup'),
    path('users/<int:user_id>/edit/', views.edit, name='edit'),
    path('users/<int:user_id>/delete/', views.delete, name='delete'),
    path('groups/<int:group_id>/edit_group/', views.edit_group, name='edit_group'),
    path('groups/<int:group_id>/delete_group/', views.delete_group, name='delete_group'),
]