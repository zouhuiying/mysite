from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from mysite.views import current_datetime
from mysite.views import hours_ahead
from django.contrib import admin  
  
admin.autodiscover()  

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^search/$','books.views.search'),
    (r'^contact/$', 'books.views.contact'),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/', admin.site.urls),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
