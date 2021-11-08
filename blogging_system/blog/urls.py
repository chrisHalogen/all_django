from . import views
from django.urls import path

app_name = 'blog'
urlpatterns = [
	path('', views.PostList.as_view(), name = 'home_page'),
	path('<slug:slug>/', views.DetailView.as_view(), name = 'post_detail')
]