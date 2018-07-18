from django.conf.urls import include, url
from . import views
urlpatterns = [
	url(r'^$', views.index, name ='index'),
	url(r'^appointment/', views.appointment),
	url(r'^log/', views.log),
	url(r'^login/$', auth_views.login, {'template_name': 'core/log.html'}, name='log'),
]