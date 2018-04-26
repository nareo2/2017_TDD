from django.conf.urls import url, patterns, include
from lists import views

urlpatterns = patterns('',
    url(r'', include('lists.urls')),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
    url(r'^$', 'lists.views.home_page', name='home'),
    url(r'^writing/', 'lists.views.writing_page', name='writing'),
)
