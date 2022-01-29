from django.urls import path, include
from .views import site
from .views import post_detail


urlpatterns = [
    path('/', site, name='home_site'),
    path('post/<int:id>/', post_detail, name='post_detail'),
    
]
