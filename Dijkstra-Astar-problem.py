import time

grid = [
          ['O', 'E', 'E', 'E', 'E'],
          ['E', 'E', 'E', 'O', 'E'],
          ['E', 'E', 'E', 'O', 'E'],
          ['E', 'E', 'E', 'O', 'E'],
          ['E', 'E', 'E', 'O', 'E']
       ]

# Rotating the grid upside down (it is harder to do when the input is not in the regular grid position)
grid = grid[::-1]

# After rotating...

# grid = [
#           ['E', 'E', 'E', 'O', 'E'],
#           ['E', 'E', 'E', 'O', 'E'],
#           ['E', 'E', 'E', 'O', 'E'],
#           ['E', 'E', 'E', 'O', 'E'],
#           ['O', 'E', 'E', 'E', 'E']
#        ]


# Defining the dimensions of the grid
max_x = len(grid[0]) - 1
max_y = len(grid) - 1

# Defining the starting and target positions
start = (0, 0)
target = (4, 2)


# Finding neighbors considering obstacles
def get_neighbors(node):
    x, y = node
    neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    return [(nx, ny) for nx, ny in neighbors if 0 <= nx <= max_x and 0 <= ny <= max_y and grid[ny][nx] != 'O']


# Dijkstra's algorithm function
def dijkstra():
    visited = set()
    distances = {(0, 0): 0}
    path = {}

    while target not in visited:
        current = min((cell for cell in distances if cell not in visited), key=distances.get)

        visited.add(current)

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                distance = distances[current] + 1
                if neighbor not in distances or distance < distances[neighbor]:
                    distances[neighbor] = distance
                    path[neighbor] = current

    dijkstra_path = []
    current = target
    while current in path:
        dijkstra_path.append(current)
        current = path[current]
    dijkstra_path.append(start)
    dijkstra_path.reverse()
    return dijkstra_path


# A star algorithm function
def a_star():
    open_set = {start}
    came_from = {}
    g_score = {start: 0}
    f_score = {start: manhattan_distance(start, target)}

    while open_set:
        current = min(open_set, key=lambda node: f_score.get(node, float('inf')))
        if current == target:
            break

        open_set.remove(current)

        for neighbor in get_neighbors(current):
            tentative_g_score = g_score.get(current, float('inf')) + 1
            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score.get(neighbor, float('inf')) + manhattan_distance(neighbor, target)
                if neighbor not in open_set:
                    open_set.add(neighbor)

    a_star_path = []
    current = target
    while current in came_from:
        a_star_path.append(current)
        current = came_from[current]
    a_star_path.append(start)
    a_star_path.reverse()
    return a_star_path


# Calculating Manhattan distance
def manhattan_distance(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return abs(x1 - x2) + abs(y1 - y2)


# Time required to run Dijkstra's algorithm
start_time = time.time()
dijkstra_path = dijkstra()
dijkstra_time = time.time() - start_time

# Time required to run A* search
start_time = time.time()
a_star_path = a_star()
a_star_time = time.time() - start_time

# Formatting the time to show in seconds with six decimal places
dijkstra_time = "{:.6f}".format(dijkstra_time)
a_star_time = "{:.6f}".format(a_star_time)

# Printing the output
print("Dijkstra path : " + " → ".join([str(coord) for coord in dijkstra_path]))
dijkstraTime = "\nDijkstra time : " + dijkstra_time + " seconds"
print(dijkstraTime)

print("\nA* path : " + " → ".join([str(coord) for coord in a_star_path]))
aStarTime = "\nA* time : " + a_star_time + " seconds"
print(aStarTime)
