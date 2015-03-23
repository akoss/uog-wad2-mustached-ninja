from django.conf.urls import patterns, include, url
from django.contrib import admin
from carwebsite import views
from django.conf import settings
from registration.backends.simple.views import RegistrationView
from django.conf.urls.static import static

# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/carwebsite/'
        return '/carwebsite/add_profile/'

urlpatterns = patterns('',
    url(r'^', include('carwebsite.urls', namespace="carwebsite")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^carwebsite/', include('carwebsite.urls')),
        #Add in this url pattern to override the default pattern in accounts.
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    (r'^accounts/', include('registration.backends.simple.urls')),)
    #+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)','serve',{'document_root': settings.MEDIA_ROOT}),)
		#+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
