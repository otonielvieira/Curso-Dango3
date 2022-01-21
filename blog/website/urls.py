from django.urls import path, include
from .views import site


urlpatterns = [
    path('/', site),
    
]
