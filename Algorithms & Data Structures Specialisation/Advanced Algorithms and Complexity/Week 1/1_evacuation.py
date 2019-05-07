# python3


class Queue:
    def __init__(self):
        self._arr = []

    def add(self, n):
        self._arr.append(n)

    def next(self):
        return self._arr.pop(0)

    def empty(self):
        return len(self._arr) == 0


class Edge:
    def __init__(self, start_node, end_node, capacity):
        self.start_node = start_node
        self.end_node = end_node
        self.capacity = capacity
        self.flow = 0
        self.inverse_edge = None

    def __repr__(self):
        return "Start Node="+str(self.start_node)+",End Node=" +\
               str(self.end_node)+",Capacity="+str(self.capacity)+",Flow="+str(self.flow)

    def can_add_flow(self):
        return self.flow < self.capacity

    def add_flow(self, flow):
        self.flow += flow
        self.inverse_edge.flow -= flow

    def max_flow(self):
        return self.capacity-self.flow


class Node:
    def __init__(self, idx):
        self.edges = []
        self.idx = idx

    def add_edge(self, edge):
        self.edges.append(edge)

    def __repr__(self):
        return str(self.idx)


class Path:
    def __init__(self, edges=None, last_node=None, max_flow=None, size=0, visited_nodes=None):
        self.edges = [] if edges is None else edges
        self.last_node = last_node
        self.max_flow = float('inf') if max_flow is None else max_flow
        self.size = size

    def split_path(self, visited_nodes, last_node_idx):
        new_paths = []

        for edge in self.last_node.edges:
            if edge.can_add_flow() and edge.end_node.idx not in visited_nodes:
                p = Path(edges=self.edges+[edge],
                         last_node=edge.end_node,
                         size=self.size+1,
                         max_flow=min(self.max_flow, edge.max_flow()))

                new_paths.append(p)
                if edge.end_node.idx != last_node_idx:
                    visited_nodes.append(edge.end_node.idx)

        return new_paths


def get_shortest_path(nodes):
    last_node_idx = len(nodes)-1
    # Initialize path
    start_path = Path(last_node=nodes[0])
    visited_nodes = [nodes[0]]
    q = Queue()
    q.add(start_path)
    final_paths = []
    while not q.empty():
        path = q.next()
        if path.last_node.idx == last_node_idx:
            final_paths.append(path)
        else:
            paths = path.split_path(visited_nodes, last_node_idx)

            for path in paths:
                q.add(path)
    if final_paths:
        res = final_paths[0]
        for p in final_paths[1:]:
            if p.size < res.size:
                res = p
        return res
    else:
        return None


def compute_max_flow(nodes):
    flow = 0
    while True:
        path = get_shortest_path(nodes)
        if path is None:
            return flow
        for edge in path.edges:
            edge.add_flow(path.max_flow)
        flow += path.max_flow


if __name__ == '__main__':
    vertex_count, edge_count = map(int, input().split())
    ns = [Node(i) for i in range(vertex_count)]
    for _ in range(edge_count):
        u, v, c = map(int, input().split())
        e = Edge(start_node=ns[u-1], end_node=ns[v-1], capacity=c)
        e_inverse = Edge(start_node=ns[v-1], end_node=ns[u-1], capacity=0)
        e.inverse_edge = e_inverse
        e_inverse.inverse_edge = e
        ns[u-1].add_edge(e)
        ns[v-1].add_edge(e_inverse)
    print(compute_max_flow(ns))
