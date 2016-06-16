from collections import defaultdict


class Circuit(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_components(connections)

    def add_components(self, connections):
        """ Add connections (list of tuple pairs) to graph """
        for node1, node2, c_type, c_value in connections:
            self.add_node(node1, node2, c_type, c_value)

    def add_node(self, node1, node2, c_type, c_value):
        """ Add connection between node1 and node2 """

        self._graph[node1].add((node2, c_type, c_value))
        if not self._directed:
            self._graph[node2].add((node1, c_type, c_value))



    def remove(self, node):
        """ Remove all references to node """

        for n, cxns in self._graph.items():
            print(n,cxns)
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """

        return node1 in self._graph and node2 in self._graph[node1]

    def find_path(self, node1, node2, path=[]):
        """ Find any path between node1 and node2 (may not be shortest) """

        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        for node in self._graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path
        return None

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))