from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from .views import HomePageView, PaginationView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scuploader.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^filelists$', PaginationView.as_view(), name='filelists'),
)
