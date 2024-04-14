from maze_visualizer import MazeVisualizer


def isFinished(status, end):
    return status == end


def dfs(start, end, maze, visualizer):
    if isFinished(start, end):
        return 0

    visual_move = (0, 0)
    visual_path = [(0, 0)]
    visual_visited = [(0, 0)]

    graph = {}
    stack = [(start, 0)]
    graph[start] = 0
    prev = {}
    prev[start] = None

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    next_status = (0, 0)

    while True:
        if not stack:
            if end in graph.keys():
                visual_move = (n - 1, m - 1)
                shortest_path = []
                temp = end
                while temp is not None:
                    shortest_path.append(temp)
                    temp = prev[temp]
                    visual_path = shortest_path
                visualizer.visualize(visual_path, visual_visited, visual_move, True, True, graph[end])
                return graph[end]
            else:
                visualizer.visualize(visual_path, visual_visited, visual_move, True, False)
                return -1

        status, depth = stack.pop()
        x, y = status

        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]

            if 0 <= a < n and 0 <= b < m and (maze[a][b] == 0 or maze[a][b] == 0.6 or maze[a][b] == 0.4):
                next_status = (a, b)
                next_depth = depth + 1
                visual_move = next_status

                if next_status not in graph or graph[next_status] >= next_depth:
                    graph[next_status] = next_depth
                    prev[next_status] = status
                    stack.append((next_status, next_depth))

                if next_status not in visual_visited or maze[a][b] == 0.4:
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

    visualizer = MazeVisualizer(maze, "DFS")

    start = (0, 0)
    end = (n - 1, m - 1)
    print(dfs(start, end, maze, visualizer))
