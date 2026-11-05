import heapq

graph = {
    "A": [("B", 1), ("C", 5)],
    "B": [("D", 4), ("E", 1)],
    "C": [("F", 3), ("G", 7)],
    "D": [],
    "E": [("G", 1)],
    "F": [],
    "G": []
}

def ucs(start, goal):

    pq = [(0, start, [start])]
    visited = set()

    while pq:

        cost, node, path = heapq.heappop(pq)

        if node == goal:
            return path, cost

        if node in visited:
            continue

        visited.add(node)

        for child, weight in graph[node]:

            if child not in visited:
                heapq.heappush(
                    pq,
                    (cost + weight, child, path + [child])
                )

    return None, float("inf")


path, cost = ucs("A", "G")

print("UCS Path:", path)
print("Total Cost:", cost)