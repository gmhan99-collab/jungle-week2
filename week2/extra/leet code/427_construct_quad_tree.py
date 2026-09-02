"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        result = []
        n = len(grid)
        # if n == 1: 
        #     result.append[1, grid[0]]
        #     return result

        isleaf = len(set(sum(grid,[])))
        if isleaf != 1 : 
            TL = [row[0:n//2] for row in grid[0:n//2]]
            TR = [row[n//2:n] for row in grid[0:n//2]]
            BL = [row[0:n//2] for row in grid[n//2 : n]]
            BR = [row[n//2:n] for row in grid[n//2 : n]]

            return Node(1,0,self.construct(TL),self.construct(TR),self.construct(BL),self.construct(BR))

        elif isleaf == 1 :
            return Node(list(set(sum(grid,[])))[0],1,None,None,None,None)