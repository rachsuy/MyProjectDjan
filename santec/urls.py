from django.conf.urls import include, url
from . import views
urlpatterns = [
	url(r'^$', views.index, name ='index'),
	url(r'^appointment/', views.appointment, name="appointment"),
	url(r'^login/$', views.login, {'template_name': 'log.html'}, name='login'),
]