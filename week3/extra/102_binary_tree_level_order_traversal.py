# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        return self.bfs(root)

    def bfs(self, Node):
        queue = []
        answer = []
        # seen = []

        if Node is not None : 
            # answer.append(Node.val)
            queue.append(Node)
        else: return []


        while queue : 

            level = []

            for _ in range(len(queue)):
                cursor = queue.pop(0)
                level.append(cursor.val)

                if cursor.left is not None:
                    queue.append(cursor.left)

                if cursor.right is not None:
                    queue.append(cursor.right)

            answer.append(level)

        return answer