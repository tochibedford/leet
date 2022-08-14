# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodeStack = [root]
        responseStack = []
        
        
        while nodeStack:
            node = nodeStack.pop()
            if node:
                responseStack.append(node.val)
                nodeStack.append(node.right)
                nodeStack.append(node.left)
        return responseStack
        
# preorder traversal of a tree is the order in which each node is visited/seen first with preference to leftward branches