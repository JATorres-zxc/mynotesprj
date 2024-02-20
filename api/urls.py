from django.urls import path
from api.views import *

urlpatterns = [
    path('', getRoutes, name='routes'),
    path('notes/', getNotes, name='getnotes'),
    path('notes/create/', createNote, name='createnote'),
    path('notes/<str:pk>/update/', updateNote, name='updatenote'),
    path('notes/<str:pk>/delete/', deleteNote, name='deletenote'),
    path('notes/<str:pk>/', getNote, name='getnote'),
]
