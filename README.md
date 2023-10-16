You’re in a grid at a starting position (0, 0). You want to reach a target position (target_x, target_y). You can only move to the top, left, bottom or right cell from a certain cell position. 

The grid’s lower left is (0, 0) and upper right is (max_x, max_y)

Each cell is either ‘E’ or ‘O’. E represents an empty cell, ‘O’ represents an obstacle. You can’t move into an obstacle. Find the shortest path to reach the target from the starting position. using Dijkstra’s algorithm and A* then find out how these two differ in terms of result and/or time in milliseconds? Were you able to reach there?

Use Manhattan distance as the heuristic. 
Manhattan distance = absolute difference between the x coordinates + absolute difference between the y coordinates.


# Input:  
Starting position: (0,0)  
Target position: (4,2)  

O E E E E  
E E E O E  
E E E O E  
E E E O E  
E E E O E  

# Note:
You may take the input in a 2D matrix like this grid =  
[   
  ['O', 'E', 'E', 'E', 'E'],  
  ['E', 'E', 'E', 'O', 'E'],  
  ['E', 'E', 'E', 'O', 'E'],  
  ['E', 'E', 'E', 'O', 'E'],  
  ['E', 'E', 'E', 'O', 'E']  
]  

Look if you access using indices, the first element i.e. grid[0][0] is ‘O’ the (0, 0) position isn’t matched with the index, (0, 0) position is actually grid[4][0]. You may use a helper method to convert the index pair to position & vice versa. 

# Hint:
Subtraction / Addition might help with the row index. Look, the row index corresponds to the y coordinate & the column index corresponds to the x coordinate. Do you need to convert the row or the column?

# Sample Output:

**A * path:**
(0,0) -> (1,0) -> (2,0) -> (2,1) -> (2,2) -> (2,3) -> (2,4) -> (3, 4) -> (4,4) -> (4,3) -> (4,2)  
**A * time:** X.XXXX sec

**Dijkstra path:**
(0,0) -> (1,0) -> (2,0) -> (2,1) -> (2,2) -> (2,3) -> (2,4) -> (3, 4) -> (4,4) -> (4,3) -> (4,2)  
**Dijkstra time:** X.XXXX sec

