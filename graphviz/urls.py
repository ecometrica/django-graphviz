from django.conf.urls.defaults import *

import views

urlpatterns = patterns('',
    (r'^dot_file/(?P<slug>.*)/$', views.dot_file, {'template':'graphviz/dot_file.dot'}),
    (r'^dot_view/(?P<slug>.*)/$', views.dot_file, {'view':True, 'template':'graphviz/dot_file.dot'}),
    (r'^image_file/(?P<slug>.*)/$', views.image_file),
)
