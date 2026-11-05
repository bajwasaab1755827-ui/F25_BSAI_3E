# Depth Limited Search (DLS)
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}

def dls(node, goal, limit, path):

    if node == goal:
        return "FOUND", path

    if limit == 0:
        if graph[node]:
            return "CUTOFF", None
        return "FAILURE", None

    cutoff = False

    for child in graph[node]:

        if child not in path:
            status, result = dls(
                child, goal, limit - 1, path + [child]
            )

            if status == "FOUND":
                return status, result

            if status == "CUTOFF":
                cutoff = True

    if cutoff:
        return "CUTOFF", None

    return "FAILURE", None


for depth in range(1, 5):
    status, path = dls("A", "G", depth, ["A"])
    print("Depth:", depth, "Status:", status, "Path:", path)







# Iterative Deepening Depth First Search (IDDFS)

def iddfs(start, goal, max_depth):

    for depth in range(1, max_depth + 1):

        status, path = dls(start, goal, depth, [start])

        print("Limit:", depth, "Status:", status)

        if status == "FOUND":
            return path

    return None


result = iddfs("A", "G", 4)

print("Final Path:", result)