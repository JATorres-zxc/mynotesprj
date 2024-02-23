from django.urls import path
from api.views import *

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('', getRoutes, name='routes'),
    path('notes/', getNotes, name='getnotes'),
    path('notes/<str:pk>/', getNote, name='getnote'),
    
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
