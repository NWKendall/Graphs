"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertext does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # queue
        q = Queue()
        q.enqueue(starting_vertex)

        visited = set()
        while q.size() > 0:
            v = q.dequeue()

            if v not in visited:
                print(v)
                visited.add(v)

                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # stack
        st = Stack()
        st.push(starting_vertex)

        visited = set()
        while st.size() > 0:
            v = st.pop()

            if v not in visited:
                print(v)
                visited.add(v)

                for next_vert in self.get_neighbors(v):
                    st.push(next_vert)

    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # base case
        if visited is None:
            visited = set()
        # track visited nodes
        visited.add(starting_vertex)
        print(starting_vertex)
        # traverse case - recurse call
        for neighbour in self.get_neighbors(starting_vertex):
            if neighbour not in visited:
                self.dft_recursive(neighbour, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create queue
        q = Queue()
        # insert first value into q (start ing v) as a LIST!!!
        q.enqueue([starting_vertex])

        # create set to store all visited nodes
        visited = set()
        # while q has is not empty
        while q.size() > 0:
            # removing head of q (a list) and sotring it in value
            path = q.dequeue()
            # storing last value in path array
            node = path[-1]
            # checking to see if node is not in visited
            if node not in visited:
                visited.add(node)
                # for each node, creating new paths for each of it's neighbours
                for neighbour in self.get_neighbors(node):
                    new_path = list(path)
                    new_path.append(neighbour)
                    q.enqueue(new_path)
                    if neighbour == destination_vertex:
                        return new_path
                        
        return "So sorry, but a connecting path doesn't exist :("

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create queue
        st = Stack()
        # insert first value into q (start ing v)
        st.push([starting_vertex])

        # create set to store all visited nodes
        visited = set()
        # while q has vs in it
        while st.size() > 0:
            # removing head of q and sotring it in value
            path = st.pop()
            node = path[-1]
            # if not visited
            if node not in visited:
                visited.add(node)
                for neighbour in self.get_neighbors(node):
                    new_path = list(path)
                    new_path.append(neighbour)
                    st.push(new_path)
                    if neighbour == destination_vertex:
                        return new_path
                        
        return "So sorry, but a connecting path doesn't exist :("

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        if visited is None:
            visited = set()
        
        if path is None:
            path = []

        visited.add(starting_vertex)
        new_path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return new_path

        for neighbour in self.get_neighbors(starting_vertex):
            if neighbour not in visited:
                neighbour_path =  self.dfs_recursive(neighbour, destination_vertex, visited, new_path)
                if neighbour_path:
                    return neighbour_path



if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
