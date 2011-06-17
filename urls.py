from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', include('intranet.springboard.urls')),
    (r'^courses/', include('courses.urls', namespace="courses", app_name="courses")),
    (r'^profiles/', include('profiles.urls', namespace="courses", app_name="profiles")),
    (r'^tinymce/', include('tinymce.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}, name="login"),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login', name="logout"),
    (r'^profiles/', include('profiles.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                             {'document_root': settings.MEDIA_ROOT,
                              'show_indexes': True}),
                            )
