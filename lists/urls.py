from django.conf.urls import url, patterns
from lists import views

urlpatterns = patterns('',
    url(r'^(\d+)/$',
        'lists.views.view_list',
        name='view_list'
    ),
    url(r'^new$', 'lists.views.new_list', name='new_list'),
)
