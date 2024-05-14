def add_edge(graph, u, v):
    if u not in graph:
        graph[u] = []
    graph[u].append(v)


def is_cyclic_util(graph, v, visited, marked):
    visited[v] = True
    marked[v] = True

    if v in graph:
        for neighbor in graph[v]:
            if not visited[neighbor]:
                if is_cyclic_util(graph, neighbor, visited, marked):
                    return True
            elif marked[neighbor]:
                return True

    marked[v] = False
    return False


def is_cyclic(graph, vertices):
    visited = {v: False for v in vertices}
    marked = {v: False for v in vertices}

    for node in vertices:
        if not visited[node]:
            if is_cyclic_util(graph, node, visited, marked):
                return True
    return False


def detect_deadlock(processes, resources, allocations, requests):
    graph = {}

    # Add edges for resource allocation
    for p, r in allocations:
        add_edge(graph, p, len(processes) + r)

    # Add edges for resource requests
    for p, r in requests:
        add_edge(graph, len(processes) + r, p)

    vertices = list(range(len(processes) + len(resources)))

    if len(allocations)==0:
        print('Deadlock detected')
    elif is_cyclic(graph, vertices):
        print("Deadlock detected!")
    else:
        print("No deadlock detected.")


# Example 
if __name__ == "__main__":
    processes = [0, 1, 2,3]
    resources = [0, 1, 2,3]
    allocations = [(0,0),(1,1),(2,2),(3,3)]
    requests = [(0, 3), (1, 2), (2, 0)]

    detect_deadlock(processes, resources, allocations, requests)
