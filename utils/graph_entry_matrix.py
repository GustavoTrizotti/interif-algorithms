def graph_entry_matrix(entry: str, v):
    num_v = len(v)
    adjacency_matrix = [[0] * num_v for _ in range(num_v)]
    lines = entry.strip().split('\n')

    for line in lines:
        parts = line.split()
        if len(parts) >= 2:
            origin_v = parts[0]
            destiny_v = parts[1]
            weight = int(parts[2]) if len(parts) >= 3 else 1
            origin_index = v.index(origin_v)
            destiny_index = v.index(destiny_v)

            adjacency_matrix[origin_index][destiny_index] = weight

    return adjacency_matrix


entry = """A B 5
C D 3
A C 2
B D 1
"""

v = ["A", "B", "C", "D"]
matriz = graph_entry_matrix(entry, v)
for line in matriz:
    print(line)
    
'''
    [0, 5, 2, 0]
    [0, 0, 0, 1]  
    [0, 0, 0, 3]  
    [0, 0, 0, 0]    
'''