import heapq
import sys

def shortest_paths(num_vertices, adjacency_list, start_vertex):
    distances = [sys.maxsize] * (num_vertices + 1)
    distances[start_vertex] = 0
    priority_queue = [(0, start_vertex)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, edge_weight in adjacency_list[current_vertex]:
            if distances[current_vertex] + edge_weight < distances[neighbor]:
                distances[neighbor] = distances[current_vertex] + edge_weight
                heapq.heappush(priority_queue, (distances[neighbor], neighbor))
    
    return distances

def main_algorithm():
    vertex_count, edge_count = map(int, input().split())
    
    vertex_links = [[] for _ in range(vertex_count + 1)]
    for _ in range(edge_count):
        from_vertex, to_vertex, weight = map(int, input().split())
        vertex_links[from_vertex].append((to_vertex, weight))
        vertex_links[to_vertex].append((from_vertex, weight))

    starting_vertex = int(input())
    vertex_distances = shortest_paths(vertex_count, vertex_links, starting_vertex)
    sum_of_distances = sum(d for d in vertex_distances[1:] if d != sys.maxsize)
    print(sum_of_distances)
    
if __name__ == "__main__":
    main_algorithm()