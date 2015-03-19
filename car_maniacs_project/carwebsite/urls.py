from django.conf.urls import patterns, url
from carwebsite import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
		url(r'^news',views.news,name='news'),
		url(r'^manufacturers',views.manufacturers,name='manufacturers'),
        url(r'^manufacturer/(?P<manufacturer_name_slug>[\w\-]+)/$', views.manufacturer, name='manufacturer'), 
        url(r'^manufacturer/(?P<manufacturer_name_slug>[\w\-]+)/(?P<model_name_slug>[\w\-]+)/$', views.model, name='model'),        
		url(r'^new_cars',views.new_cars,name='new_cars'),
		url(r'^compare',views.compare,name='compare'),
        url(r'^top_rated',views.top_rated,name='top_rated'),
        url(r'^search',views.search,name='search'),
		)
