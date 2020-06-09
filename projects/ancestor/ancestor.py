class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertext does not exist")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

def earliest_ancestor(ancestors, starting_node):
    
    graph = Graph()

    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

        graph.add_edge(pair[1], pair[0])


    q = Queue()
    q.enqueue([starting_node])
    max_path_len = 1
    earliest_ancestor = -1

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        print("Path", path)
        print("EA1", earliest_ancestor)

        if (len(path) >= max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
            print("EA2", earliest_ancestor)
            max_path_len = len(path)
            earliest_ancestor = v
            print("EA3", earliest_ancestor)

        for neighbour in graph.get_neighbors(v):
            new_path = list(path)
            new_path.append(neighbour)
            print("NP", new_path)
            q.enqueue(new_path)

    print("dict", graph.vertices)

    return earliest_ancestor









# need node class?
    # value, left, right
# search for starting node
# go down tree from stargin node to find LCA
# recieve [(paren, child)...], target
# return int

l = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(l, 6))