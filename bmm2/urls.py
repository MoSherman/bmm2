from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'bmm2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'museum.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
]
