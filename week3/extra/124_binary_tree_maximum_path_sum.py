# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        u, i = self.dfs(root)

        return max(u, i)
                
    def dfs(self, node):
        # 입력이 0 = head
        # 0 * 2 + 1 = head.left
        # 0 * 2 + 2 = head.right

        if node is None: return 0, float("-inf")

        if node.left is None and node.right is None : return node.val, node.val

        # return max(self.dfs(node.left) + node.data, self.dfs(node.right) + node.data)
        # return max(node.data + max(max(0, self.dfs(node.left), max(0, self.dfs(node.right)))))
        left, max_left = self.dfs(node.left)
        right, max_right = self.dfs(node.right)

        left_p = max(0,left)
        right_p = max(0,right)

        mid = left_p + node.val + right_p # 부모에게 반환하지 않을 경우?

        max_answer = max(max_left, max_right, mid)

        to_parents = node.val + max(left_p, right_p)

    
        return to_parents, max_answer