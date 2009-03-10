from django.db import models

# The following interfaces may be used
# it is not required but good for understanding
from django_graphviz.graphviz.interfaces import IGraphRoot, IEdge, INode

class People(models.Model, IGraphRoot, INode):
    ''' this models is used as a graph root and as a node.
    '''
    name = models.CharField(max_length=50)
    
    def gv_edges(self, graph):
        links = list(Relationship.objects.all())
        links.extend(self.car_set.all())
        return links
    
    def gv_nodes(self, graph):
        nodes = list(People.objects.all())
        nodes.extend(self.car_set.all())
        return nodes
    
    def __unicode__(self):
        return self.name
        

class Relationship(models.Model, IEdge):
    ''' this models is a typical edge.
    '''
    type = models.CharField(max_length=50)
    source = models.ForeignKey(People, related_name='src_relation_set')    
    target = models.ForeignKey(People, related_name='tgt_relation_set')
    
    def gv_ends(self, graph):
        return (self.source, self.target)
    
    def gv_edge_label(self, graph):
        return self.type
    
    def __unicode__(self):
        return str(self.pk)
    
class Car(models.Model, INode, IEdge):
    ''' this models is used as a node and as an edge (ownership).
    '''
    type = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    owner = models.ForeignKey(People)
    
    def gv_ends(self, graph):
        return (self, self.owner)
    
    def gv_edge_label(self, graph):
        return 'belongs to'
    
    def __unicode__(self):
        return self.type
