import numpy as np
from copy import copy
from random import sample

class Game():
    def __init__(self):
        self.grid = np.zeros((4,4),dtype='int')
        self.reset_idx_empty()
        self.random_fill()
        self.random_fill()
        return None
    
    def random_fill(self):
        idx_fill = sample(self.idx_empty, 1)
        self.grid[idx_fill[0]] = 2**np.random.randint(1, 3, size=1)
        self.reset_idx_empty()
        return None
    
    def reset_idx_empty(self):
        rows, cols = np.where(self.grid==0)
        self.idx_empty = set(zip(rows, cols))
        return None
    
    def check_over(self):
        pass
    
    def make_move(self, action):
        grid0 = copy(self.grid)
        
        def _proc_array(a):
            
            non_zero = list(filter(lambda x: x!=0, a))
            completed = []
            
            while len(non_zero)>1:
                if non_zero[-1] == non_zero[-2]:
                    completed.append(2*non_zero[-1])
                    non_zero = non_zero[:-2]
                else:
                    completed.append(non_zero[-1])
                    non_zero = non_zero[:-1]

            n_zero = len(a) - len(non_zero) - len(completed)
            return [0]*n_zero + non_zero + list(reversed(completed))
        
        _reverse_array = lambda a: np.array(list(reversed(a)))
        
        _proc_inverted = lambda a: _reverse_array(_proc_array(_reverse_array(a)))
        
        if action == 'right':
            for i in range(4):
                self.grid[i,:] = _proc_array(self.grid[i,:])
        elif action == 'down':
            for i in range(4):
                self.grid[:,i] = _proc_array(self.grid[:,i])
        elif action == 'left':
            for i in range(4):
                self.grid[i,:] = _proc_inverted(self.grid[i,:])
        elif action == 'up':
            for i in range(4):
                self.grid[:,i] = _proc_inverted(self.grid[:,i])
        else:
            print('That is not a valid action.')
            return None
        
        if np.prod(grid0 == self.grid):
            print('The action ' + action + ' does not affect the current grid.')
            return None
            
        self.random_fill()
        self.reset_idx_empty()
        
        return None
