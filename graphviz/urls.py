from django.conf.urls import patterns

from .views import dot_file, image_file

urlpatterns = patterns('',
    (r'^dot_file/(?P<slug>.*)/$', dot_file, {'template':'graphviz/dot_file.dot'}),
    (r'^dot_view/(?P<slug>.*)/$', dot_file, {'view':True, 'template':'graphviz/dot_file.dot'}),
    (r'^image_file/(?P<slug>.*)/$', image_file),
)
