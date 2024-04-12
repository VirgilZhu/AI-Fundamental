def isFinished(status, end):
    return status == end

def dfs(start, end, maze):
    if isFinished(start, end):
        return 0

    graph = {}
    stack = []
    stack.append((start, 0))
    graph[start] = 0

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    next_status = (0, 0)

    while True:
        if stack == []:
            if end in graph.keys():
                return graph[end]
            else:
                return -1

        status, depth = stack.pop()
        x, y = status

        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < n and 0 <= b < m and (maze[a][b] == 0):
                next_status = (a, b)
                next_depth = depth + 1
                if next_status not in graph or graph[next_status] >= next_depth:
                    graph[next_status] = next_depth
                    stack.append((next_status, next_depth))

n, m = map(int, input().split())
maze = []
for i in range(n):
    row = list(map(int, input().split()))
    maze.append(row)

start = (0, 0)
end = (n - 1, m - 1)
print(dfs(start, end, maze))
