import heapq

def isFinished(status, end):
    return status == end

def manhattan_distance(status, end):
    return abs(status[0] - end[0]) + abs(status[1] - end[1])

def a_star(start, end, maze):
    if isFinished(start, end):
        return 0

    graph = {}
    open_list = []
    heapq.heappush(open_list, (0, start))
    graph[start] = 0

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while open_list:
        _, status = heapq.heappop(open_list)
        x, y = status

        if status == end:
            return graph[status]

        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < n and 0 <= b < m and (maze[a][b] == 0):
                next_status = (a, b)
                next_dist = graph[status] + 1
                if next_status not in graph or graph[next_status] > next_dist:
                    graph[next_status] = next_dist
                    priority = next_dist + manhattan_distance(next_status, end)
                    heapq.heappush(open_list, (priority, next_status))

n, m = map(int, input().split())
maze = []
for i in range(n):
    row = list(map(int, input().split()))
    maze.append(row)

start = (0, 0)
end = (n - 1, m - 1)
print(a_star(start, end, maze))
