"""
"""

   
class IGraphRoot:
    def gv_edges(self, graph):
        raise Exception('not implemented') 
    def gv_nodes(self, graph):
        raise Exception('not implemented') 

class INode:
    def gv_node_label(self, graph):
        return unicode(self)

class IEdge:
    def gv_ends(self, graph):
        ''' should returns (node_source, node_target)
        '''
        raise Exception('not implemented') 
    def gv_edge_label(self, graph):
        return unicode(self)
