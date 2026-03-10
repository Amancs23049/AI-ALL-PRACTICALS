
graph = {
    'S': [('A', 1), ('D', 13)],
    'A': [('B', 2), ('C', 5)],
    'B': [('C', 2)],
    'C': [('D', 3)],
    'D': []
}

h = {'S': 7, 'A': 6, 'B': 2, 'C': 1, 'D': 0}


def astar(start, goal):
    open = [start]
    cost = {start: 0}
    parent = {start: None}

    while open:
        current = open[0]
        for n in open:
            if cost[n] + h[n] < cost[current] + h[current]:
                current = n

        open.remove(current)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1], cost[goal]

        for next, w in graph[current]:
            new_cost = cost[current] + w
            if next not in cost or new_cost < cost[next]:
                cost[next] = new_cost
                parent[next] = current
                open.append(next)


def bfs(start, goal):
    queue = [start]
    parent = {start: None}

    while queue:
        current = queue.pop(0)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for next, _ in graph[current]:
            if next not in parent:
                parent[next] = current
                queue.append(next)

start_node = input("Enter start node: ")
goal_node = input("Enter goal node: ")

a_path, a_cost = astar(start_node, goal_node)
b_path = bfs(start_node, goal_node)

print("\nA* Algorithm Output")
print("Path:", a_path)
print("Shortest Path Cost:", a_cost)

print("\nBFS Algorithm Output")
print("Path:", b_path)
