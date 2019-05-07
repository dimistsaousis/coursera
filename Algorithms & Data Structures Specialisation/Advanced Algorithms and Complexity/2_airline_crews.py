"""
Task. The airline offers a bunch of flights and has a set of crews that can work on those flights. However,
the flights are starting in different cities and at different times, so only some of the crews are able to
work on a particular flight. You are given the pairs of flights and associated crews that can work on
those flights. You need to assign crews to as many flights as possible and output all the assignments.

Input Format. The first line of the input contains integers 𝑛 and 𝑚 — the number of flights and the number
of crews respectively. Each of the next 𝑛 lines contains 𝑚 binary integers (0 or 1). If the 𝑗-th integer
in the 𝑖-th line is 1, then the crew number 𝑗 can work on the flight number 𝑖, and if it is 0, then it
cannot.

Constraints. 1 ≤ 𝑛, 𝑚 ≤ 100.

Output Format. Output 𝑛 integers — for each flight, output the 1-based index of the crew assigned to
this flight. If no crew is assigned to a flight, output −1 as the index of the crew corresponding to it.
All the positive indices in the output must be between 1 and 𝑚, and they must be pairwise different,
but you can output any number of −1’s. If there are several assignments with the maximum possible
number of flights having a crew assigned, output any of them.
"""


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
    def __init__(self, edges=None, last_node=None, max_flow=None, size=0):
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
            return nodes
        for edge in path.edges:
            edge.add_flow(path.max_flow)
        flow += path.max_flow


def assign_flights_to_crew(nodes, flight_no):
    res = []
    for i in range(1, flight_no+1):
        node = nodes[i]
        found = False
        for edge in node.edges:
            if edge.flow == 1:
                res.append(str(edge.end_node.idx-flight_no))
                found = True
                break
        if not found:
            res.append(str(-1))
    return res


def create_edge_and_inverse(start_node, end_node, capacity):
    e_ = Edge(start_node, end_node, capacity)
    e_inverse = Edge(end_node, start_node, 0)
    e_.inverse_edge = e_inverse
    e_inverse.inverse_edge = e_
    return e_, e_inverse


if __name__ == '__main__':
    number_of_flights, number_of_crew = map(int, input().split())
    ns = [Node(i) for i in range(number_of_flights+number_of_crew+2)]

    # Add crew to sink
    for j in range(number_of_crew):
        e, ei = create_edge_and_inverse(ns[number_of_flights + j + 1], ns[-1], capacity=1)
        ns[number_of_flights + j + 1].add_edge(e)
        ns[-1].add_edge(ei)

    for i in range(1, number_of_flights+1):
        crew_assignments = list(map(int, input().split()))
        # Connect flight to source
        e, ei = create_edge_and_inverse(ns[0], ns[i], capacity=1)
        ns[0].add_edge(e)
        ns[i].add_edge(ei)

        # Connect flight to crew
        for j in range(number_of_crew):
            if crew_assignments[j] == 1:
                e, ei = create_edge_and_inverse(ns[i], ns[number_of_flights+j+1], capacity=1)
                ns[i].add_edge(e)
                ns[number_of_flights+j+1].add_edge(ei)
    ns = compute_max_flow(ns)
    result = assign_flights_to_crew(ns, number_of_flights)
    print(' '.join(result))
