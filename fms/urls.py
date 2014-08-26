from django.conf.urls import patterns, include, url
import fms_app
from fms_app.views import logout_user
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    
    #url(r'^$', 'fms.views.home', name='home'),
    url(r'^fms/', include('fms_app.urls')),
     url(r'^admission/', include('admission_app.urls')),
   

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^fms/logout/', logout_user , name = "logout"),
    url(r'^admin/', include(admin.site.urls)),
)
