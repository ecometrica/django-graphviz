from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Graph

class TEdge:
    def __init__(self, data, graph):
        self.start_node, self.end_node = data.gv_ends(graph)
        self.start_node_label = self.start_node.gv_node_label(graph)
        self.end_node_label = self.end_node.gv_node_label(graph)
class TGraph:
    def __init__(self, graph):
        self.edges = []
        for e in graph.content_object.gv_edges(graph):
            self.edges.append(TEdge(e, graph))

def dot_file(request, slug, template='graphviz/dot_file.dot'):
    graph = Graph.objects.get(slug=slug)
    context = {'graph':TGraph(graph)}
    response = render_to_response(template, context, mimetype='text/plain',
                                  context_instance=RequestContext(request))
    response['Content-Disposition'] = 'attachment; filename=%s.dot' % slug
    return response

def image_file(request, slug, template='graphviz/dot_file.html'):
    return HttpResponse('todo image')