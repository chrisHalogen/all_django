from django.urls import include, path
from django.conf.urls import url

from .views import index, profile, logout

app_name = 'user_app'

urlpatterns = [
    path('', index ,name = 'index'),
    path('profile/', profile ,name = 'profile'),
    url(r'^',include('social_django.urls',namespace='social')),
    path('logout/',logout, name = 'logout')
]