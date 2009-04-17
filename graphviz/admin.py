from django.contrib import admin
from models import *

class GraphAdmin(admin.ModelAdmin):
   list_display = ('slug', 'name', 'content_type', 'view_dot_file', 'download_dot_file', 'download_image')
   list_filter = ('content_type',)
admin.site.register(Graph, GraphAdmin)


class NodeVisualAdmin(admin.ModelAdmin):
   list_display = ('name', 'shape', 'options', 'graph', 'content_type')
   list_filter = ('content_type', 'graph')
   save_as = True
admin.site.register(NodeVisual, NodeVisualAdmin)


class ArrowVisualAdmin(admin.ModelAdmin):
   list_display = ('shape', 'modifier', 'graph', 'content_type')
   list_filter = ('content_type', 'graph')
   save_as = True
admin.site.register(ArrowVisual, ArrowVisualAdmin)


class CacheImageAdmin(admin.ModelAdmin):
   list_display = ('graph', 'graphic', 'valid', 'file', 'date')
   list_filter = ('valid', 'graph')
admin.site.register(CacheImage, CacheImageAdmin)
