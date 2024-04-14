import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox


def show_message_box(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("搜索完毕", message)
    root.destroy()


class MazeVisualizer:
    def __init__(self, maze, title):
        self.maze = maze
        self.title = title
        self.first_call = True
        self.fig, self.ax = plt.subplots(figsize=(len(maze[0]), len(maze)))
        self.im = self.ax.imshow(maze, cmap='Greys', interpolation='nearest')
        self.path_line, = self.ax.plot([], [], marker='o', markersize=8, color='red', linewidth=3)
        self.move_point, = self.ax.plot([], [], marker='o', markersize=8, color='yellow')

        # 设置坐标轴刻度和边框
        self.ax.set_xticks(range(len(maze[0])))
        self.ax.set_yticks(range(len(maze)))
        self.ax.set_xticks([x - 0.5 for x in range(1, len(maze[0]))], minor=True)
        self.ax.set_yticks([y - 0.5 for y in range(1, len(maze))], minor=True)
        self.ax.grid(which="minor", color="black", linestyle='-', linewidth=2)

    def visualize(self, path=[], visited=[], move=None, last_call=False, issolvable=False, steps=0):
        if self.first_call:
            self.fig.suptitle(self.title, fontsize=20)
            self.first_call = False

        if move:
            move_x, move_y = move
            self.move_point.set_data(move_y, move_x)

        if visited:
            visited_x, visited_y = zip(*visited)
            for x, y in zip(visited_x, visited_y):
                self.maze[x][y] = 0.4

        if path:
            path_x, path_y = zip(*path)
            for x, y in zip(path_x, path_y):
                self.maze[x][y] = 0.6
            self.path_line.set_data(path_y, path_x)

        self.im.set_data(self.maze)
        self.fig.canvas.draw()
        if not last_call:
            plt.pause(0.3)
        else:
            message = ""
            if issolvable is True:
                message += ("共需移动" + str(steps) + "步。")
            else:
                message += "迷宫不可解。"
            show_message_box(message)
            plt.show()
