from Maze_generator import *

# Geel = start, Groen = uitgang

maze1 = Maze()
maze1.grid(20, 10)
maze1.in_en_uitgang()
maze1.genereer_wegen()
maze1.print_maze()
