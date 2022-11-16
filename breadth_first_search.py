import numpy as np
from helpers import Action, valid_actions, visualize_path
from queue import Queue

def testBDF():
  start = []
  end = []
  for i in range(2):
      elm = input(f'Enter start location {i+1}: ')
      start.append(int(elm))
  
  print(start)
  
  for i in range(2):
      elm = input(f'Enter goal location {i+1}: ')
      end.append(int(elm))
  print(end)
  
  grid = np.array([
      [0, 1, 0, 0, 0, 0],
      [0, 1, 0, 0, 0, 0],
      [0, 1, 0, 1, 0, 0],
      [0, 0, 0, 1, 1, 0],
      [0, 0, 0, 1, 0, 0],
  ])
  
  print(
      visualize_path(grid, breadth_first(grid, tuple(start), tuple(end)),
                   tuple(start)))

def breadth_first(grid, start, goal):
    q = Queue()
    q.put(start) 
    visited = set()
    visited.add(start)
    branch = {}
    found = False
    
    # Run loop while queue is not empty
    while not q.empty():
        current_node = q.get()
        if current_node == goal: 
            print('Found a path.')
            found = True
            break
        else:
            valid = valid_actions(grid, current_node)
            for action in valid:
                # delta of performing the action
                da = action.value
                next_node = (current_node[0] + da[0], current_node[1] + da[1])

                if next_node not in visited:                
                    visited.add(next_node)               
                    q.put(next_node)          
                    branch[next_node] = (current_node, action) 
    path = []
    if found:
        # retrace steps
        path = []
        n = goal
        while branch[n][0] != start:
            path.append(branch[n][1])
            n = branch[n][0]
        path.append(branch[n][1])
            
    return path[::-1]