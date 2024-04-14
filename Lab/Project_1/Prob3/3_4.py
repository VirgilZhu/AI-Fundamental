import heapq
from maze_visualizer import MazeVisualizer


def isFinished(status, end):
    return status == end


def manhattan_distance(status, end):
    return abs(status[0] - end[0]) + abs(status[1] - end[1])


def a_star(start, end, maze, visualizer):
    if isFinished(start, end):
        return 0

    visual_move = (0, 0)
    visual_path = [(0, 0)]
    visual_visited = [(0, 0)]

    graph = {}
    visited = {}
    open_list = []
    heapq.heappush(open_list, (0, start))
    graph[start] = 0
    visited[start] = False
    prev = {}
    prev[start] = None

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while True:
        if len(open_list) == 0:
            visualizer.visualize(visual_path, visual_visited, visual_move, True, False)
            return -1

        _, status = heapq.heappop(open_list)

        if visited[status] is True:
            continue

        visited[status] = True
        x, y = status

        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < n and 0 <= b < m and (maze[a][b] == 0):
                next_status = (a, b)
                next_dist = graph[status] + 1
                visual_move = next_status

                if next_status not in visited or visited[next_status] is False or (visited[next_status] is True and graph[next_status] > next_dist):
                    visited[next_status] = False
                    graph[next_status] = next_dist
                    prev[next_status] = status
                    priority = next_dist + manhattan_distance(next_status, end)
                    heapq.heappush(open_list, (priority, next_status))

                if isFinished(next_status, end):
                    shortest_path = []
                    temp = next_status
                    while temp is not None:
                        shortest_path.append(temp)
                        temp = prev[temp]
                        visual_path = shortest_path
                    visualizer.visualize(visual_path, visual_visited, visual_move, True, True, graph[next_status])
                    return graph[next_status]

                if next_status not in visual_visited:
                    visual_visited.append(next_status)
                    shortest_path = []
                    temp = next_status
                    while temp is not None:
                        shortest_path.append(temp)
                        if temp not in prev:
                            break
                        temp = prev[temp]
                    visual_path = shortest_path
                    visualizer.visualize(visual_path, visual_visited, visual_move)


if __name__ == '__main__':
    n, m = map(int, input().split())
    maze = []
    for i in range(n):
        row = list(map(int, input().split()))
        maze.append(row)

    visualizer = MazeVisualizer(maze, "A-Star Algorithm")

    start = (0, 0)
    end = (n - 1, m - 1)
    print(a_star(start, end, maze, visualizer))