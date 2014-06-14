from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'Xpera.views.home', name='home'),
    # url(r'^Xpera/', include('Xpera.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # MediaURL
    url(
        r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        {
            'document_root': settings.MEDIA_ROOT,
        }
    ),

    url(
        r'^event/',
        include(
            'apps.event.urls',
            namespace='event',
            app_name='event'
        )
    ),

    url(
        r'^account/',
        include(
            'apps.account.urls',
            namespace='account',
            app_name='account'
        )
    ),
)
