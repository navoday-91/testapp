from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^expression$', views.expression),
    url(r'^expression/$', views.expression),
	url(r'^details/(?P<todo_id>\w{0,50})/$', views.details)
	]
