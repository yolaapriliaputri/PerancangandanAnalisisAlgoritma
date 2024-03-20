# Dijkstra's Algorithm in Python

import sys

# Definisi graf dalam bentuk adjacency matrix
graph = [
    [0, 1, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0],
    [1, 1, 0, 1, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 1, 0]
]

# Algoritma Dijkstra
def dijkstra(graph, source):
    num_vertices = len(graph)
    distances = [sys.maxsize] * num_vertices
    distances[source] = 0
    visited = [False] * num_vertices

    for _ in range(num_vertices):
        min_distance = sys.maxsize
        min_index = -1
        for v in range(num_vertices):
            if not visited[v] and distances[v] < min_distance:
                min_distance = distances[v]
                min_index = v
        visited[min_index] = True

        for v in range(num_vertices):
            if not visited[v] and graph[min_index][v] and distances[min_index] + graph[min_index][v] < distances[v]:
                distances[v] = distances[min_index] + graph[min_index][v]

    return distances

# Fungsi untuk mengkonversi indeks menjadi label node
def index_to_label(index):
    return chr(ord('A') + index)

# Menggunakan fungsi Dijkstra
source_node = 0  # A
shortest_distances = dijkstra(graph, source_node)

# Menampilkan jarak terpendek dari node sumber ke semua node lain
for i, distance in enumerate(shortest_distances):
    print(f"Distance from {index_to_label(source_node)} to {index_to_label(i)}:", distance)
