from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'testem.views.home', name='home'),
    url(r'^registration/', include('registration.urls')),
    url(r'^mytests/', include('questionnaires.urls')),
    url(r'^mymaterials/', include('materials.urls')),
    url(r'^feedback/', include('feedback.urls')),
    url(r'^captcha/', include('captcha.urls')),
    # url(r'^blog/', include('blog.urls')),
    url(r'^tests/$', 'questionnaires.views.questionnaires_list', name='questionnaires_list'),
    url(r'^tests/page/(?P<page>[1-9]\d*)/$', 'questionnaires.views.questionnaires_list'),
    url(r'^myprofile/$', include('myprofile.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

#  Frontend authorization
urlpatterns += patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
)

if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
        url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns