from django.urls import path
from api.views import *

from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('', getRoutes, name='routes'), # route for all available urls
    path('notes/', getNotes, name='getnotes'), # for all notes
    path('notes/<str:pk>/', getNote, name='getnote'), # for specific note
    
    # JWT (JSON Web Tokens) provide a compact, secure way to transmit authentication 
    # information between parties in web applications without needing to store 
    # session state on the server.
    
    # i didnt use the normal obtaintokenview since i have differenct need(i need username)
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'), # route to obtain jwt token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # route to refresh jwt token
]
