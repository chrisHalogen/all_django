from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='Routes'),
    path('notes/', views.getNotes, name='Notes'),
    #  path('notes/create', views.createNote, name = 'createNotes'),
    path('notes/new/', views.createNote, name='makeNew' ),
    path('notes/<int:pk>/update', views.updateNote, name='updateNote'),
    path('notes/<int:pk>/delete', views.deleteNote, name='deleteNote'),
    path('notes/<int:pk>/', views.getNote, name='Note'),
]