from django.conf.urls import patterns, url
from carwebsite import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
		url(r'^news',views.news,name='news'),
		url(r'^manufacturers',views.manufacturers,name='manufacturers'),
		url(r'^new_cars',views.new_cars,name='new_cars'),
		url(r'^compare',views.compare,name='compare'),
		)