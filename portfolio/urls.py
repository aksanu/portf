from django.urls import path
from . import views
urlpatterns= [
	path('', views.home, name= 'index'),
	path('upload', views.upload , name= 'upload'),
	path('details/<int:id>', views.details , name= 'detail'),
	path('upload/<int:id>', views.more_upload , name= 'more_upload'),
	path('login', views.login , name= 'login'),
	path('logout', views.logout , name= 'logout'),


]