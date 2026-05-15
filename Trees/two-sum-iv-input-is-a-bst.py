from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        q = deque([root])
        seen = set()
        
        while q:
            n = q.popleft()

            v = k - n.val
            if v in seen:
                return True

            seen.add(n.val)

            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

        return False