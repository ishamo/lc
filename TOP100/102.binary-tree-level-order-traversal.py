# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root: return result
        cache = [root]
        while cache:
            result.append([item.val for item in cache])
            lenc = len(cache)
            for i in cache[:lenc]:
                if i.left:
                    cache.append(i.left)
                if i.right:
                    cache.append(i.right)

            cache = cache[lenc:]

        return result
