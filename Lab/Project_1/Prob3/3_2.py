from maze_visualizer import MazeVisualizer


def isFinished(status, end):
    return status == end


def bfs(start, end, maze, visualizer):
    if isFinished(start, end):
        return 0

    visual_move = (0, 0)
    visual_path = [(0, 0)]
    visual_visited = [(0, 0)]

    graph = {}
    queue = [(start, 0)]
    graph[start] = 0
    prev = {}
    prev[start] = None

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    next_status = (0, 0)

    while True:
        if len(queue) == 0:
            visualizer.visualize(visual_path, visual_visited, visual_move, True, False)
            return -1

        status, depth = queue.pop(0)
        x, y = status

        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < n and 0 <= b < m and (maze[a][b] == 0):
                next_status = (a, b)
                next_depth = depth + 1
                visual_move = next_status

                if next_status not in graph:
                    graph[next_status] = next_depth
                    prev[next_status] = status
                    queue.append((next_status, next_depth))
                    if isFinished(next_status, end):
                        shortest_path = []
                        temp = next_status
                        while temp is not None:
                            shortest_path.append(temp)
                            temp = prev[temp]
                            visual_path = shortest_path
                        visualizer.visualize(visual_path, visual_visited, visual_move, True, True, next_depth)
                        return next_depth

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

    visualizer = MazeVisualizer(maze, "BFS")

    start = (0, 0)
    end = (n - 1, m - 1)
    print(bfs(start, end, maze, visualizer))
