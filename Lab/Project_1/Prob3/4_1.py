def isFinished(status, end):
    return status == end

def bfs(start, end, maze):
    if isFinished(start, end):
        return 0

    graph = {}
    queue = []
    queue.append((start, 0))
    graph[start] = 0

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    next_status = (0, 0)

    while True:
        if len(queue) == 0:
            return -1

        status, depth = queue.pop(0)
        x, y = status

        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < n and 0 <= b < m and (maze[a][b] == 0):
                next_status = (a, b)
                next_depth = depth + 1
                if next_status not in graph:
                    graph[next_status] = next_depth
                    queue.append((next_status, next_depth))
                    if isFinished(next_status, end):
                        return next_depth

n, m = map(int, input().split())
maze = []
for i in range(n):
    row = list(map(int, input().split()))
    maze.append(row)

start = (0, 0)
end = (n - 1, m - 1)
print(bfs(start, end, maze))
