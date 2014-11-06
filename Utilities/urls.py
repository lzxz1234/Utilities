from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'Utilities.view.index'),
    url(r'^hello/$', 'Utilities.view.app'),
    url(r'^about/$', TemplateView.as_view(template_name="about.html")),
    url(r'^func/(.+)$', 'Utilities.view.func'),
    url(r'^qrcode', 'Utilities.view.qrcode'),
    url(r'^ip', 'Utilities.http.ip'),
    url(r'^meta', 'Utilities.http.meta'),
    # Examples:
    # url(r'^$', 'Utilities.views.home', name='home'),
    # url(r'^Utilities/', include('Utilities.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
