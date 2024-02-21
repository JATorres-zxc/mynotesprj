from django.urls import path
from api.views import *

urlpatterns = [
    path('', getRoutes, name='routes'),
    path('notes/', getNotes, name='getnotes'),
    path('notes/<str:pk>/', getNote, name='getnote'),
]
