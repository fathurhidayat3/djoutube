from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	# url(r'^[\w_.!?=@#$%^&*/:-]+/$', views.home, name='home'),
	# url(r'^(?P<furl>[\w_.!?=@#$%^&*/:-]+)/$', views.nghome, name='nghome'),
	url(r'^ng/home/(?P<furl>[\w_.!?=@#$%^&*/:-]+)/$', views.nghome, name='nghome'),
	url(r'^search/$', views.search, name='search'),
	url(r'^ng/search/(?P<fquery>[\w_ .!?=@#$%^&*/:-]+)/$', views.ngsearch, name='ngsearch'),
]
