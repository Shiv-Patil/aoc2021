connections = dict()
while inp := input():
    connection = (*inp.split("-"),)
    connections[connection[0]] = connections.get(connection[0], []) + [connection[1]]
    connections[connection[1]] = connections.get(connection[1], []) + [connection[0]]


def get_paths(connections, current, visited, last_visited):
    if current == "end":
        return 1
    if current == "start" and len(visited):
        return 0
    if current.islower() and current in visited:
        if not last_visited:
            last_visited = current
        else:
            return 0
    visited = visited.union({current})
    paths = 0
    for connection in connections[current]:
        paths += get_paths(connections, connection, visited, last_visited)
    return paths


path_count = get_paths(connections, "start", set(), "")
print("***", path_count, "***")
