def print_distance(distance, src):
    print(f"Vertex\tShortest Distance from vertex {src}")
    for i, d in enumerate(distance):
        print(f"{i}\t\t{d}")

def check_negative_cycle(graph, distance, edge_count):
    for j in range(edge_count):
        u, v, w = (graph[j][k] for k in ["src", "dst", "weight"])
        if distance[u] != float("inf") and distance[u] + w < distance[v]:
            return True
    return False

def bellman_for(graph, vertex_count, edge_count, src):
    distance = [float("inf")] * vertex_count
    distance[src] = 0.0

    for _ in range(vertex_count - 1):
        for j in range(edge_count):
            u, v, w = (graph[j][k] for k in ["src", "dst", "weight"])
            if distance[u] != float("inf") and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
    negative_cycle_exists = check_negative_cycle(graph, distance, edge_count)
    if negative_cycle_exists:
        raise Exception("Negative cycle found")
    return distance

'''
    edges = [(2, 1, -10), (3, 2, 3), (0, 3, 5), (0, 1, 4)]
    g = [{"src": s, "dst": d, "weight": w} for s, d, w in edges]
    bellman_ford(g, 4, 4, 0)
    > [0.0, -2.0, 8.0, 5.0]
'''