# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def checkTree(p,q):
            if not p :
                if not q:
                    return True
                return False

            elif not q:
                if not p:
                    return True
                return False

            else:
                if p.val==q.val:
                    left=checkTree(p.left,q.left)
                    right=checkTree(p.right,q.right)
                    return left and right
                return False
                
        return checkTree(p,q)


        