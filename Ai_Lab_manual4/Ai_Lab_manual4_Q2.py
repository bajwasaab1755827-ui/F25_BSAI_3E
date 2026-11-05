import heapq

def search(graph, h, start, goal):
    pq = [(h[start], 0, start, [start])]
    best = {start: 0}
    processed = []
    expanded = 0

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if g != best[node]:
            continue

        processed.append(node)

        if node == goal:
            return path, g, processed, expanded

        expanded += 1

        for nxt, w in graph.get(node, []):
            new_g = g + w

            if new_g < best.get(nxt, float("inf")):
                best[nxt] = new_g
                heapq.heappush(
                    pq, (new_g + h[nxt], new_g,
                         nxt, path + [nxt])
                )

graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": []
}

h = {"S": 5, "A": 4, "B": 4, "C": 2, "G": 0}

print("A*:", search(graph, h, "S", "G"))

zero_h = {node: 0 for node in graph}
print("UCS:", search(graph, zero_h, "S", "G"))