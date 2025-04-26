import heapq
n = 4
graph = {
    0: [(1, 1), (2, 3)],
    1: [(0, 1), (2, 1), (3, 4)],
    2: [(0, 3), (1, 1), (3, 2)],
    3: [(1, 4), (2, 2)]
}
def dijkstra(src):
    dist = [float('inf')] * n
    dist[src] = 0
    queue = [(0, src)]
    while queue:
        current_dist, u = heapq.heappop(queue)
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(queue, (dist[v], v))
    return dist
for i in range(n):
    distances = dijkstra(i)
    print(f"Router {i}'s Table: {distances}")
