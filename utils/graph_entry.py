def graph_entry(entry: str) -> list:
    adjacency_list = {}
    lines = entry.strip().split('\n')

    for line in lines:
        parts = line.split()
        if len(parts) >= 2:
            origin_v = parts[0]
            destiny_v = parts[1]
            peso = int(parts[2]) if len(parts) >= 3 else 1  # Peso padrão de 1 se não for fornecido

            if origin_v not in adjacency_list:
                adjacency_list[origin_v] = []

            adjacency_list[origin_v].append((destiny_v, peso))

    return adjacency_list

entry = """A B 5
C D 3
A C 2
B D 1
"""

graph = graph_entry(entry)
print(graph)

# >>> {'A': [('B', 5), ('C', 2)], 'C': [('D', 3)], 'B': [('D', 1)]}