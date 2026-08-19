# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        arr = []
        def nodes(node):
            left = 0
            right = 0
            if node is None:
                return None
            arr.append(node.val)
            left  = node.left
            right = node.right
            nodes(left)
            nodes(right)
        nodes(root1)
        nodes(root2)
        return sorted(arr)