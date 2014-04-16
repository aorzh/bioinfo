from django.conf.urls import patterns, include, url
from statistic import views
from bioinfo import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.MEDIA_ROOT}),
                       url(r'^$', views.index, name='index'),
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^logout/$', views.user_logout, name='logout'),
                       url(r'^statistic/$', views.stats, name='statistic'),
                       url(r'^profile/(?P<user_id>\d+)/$', views.profile, name='profile'),
                       url(r'^users/$', views.users_list, name='users'),
                       )
