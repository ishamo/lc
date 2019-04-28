# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        if not root: return ret
        queue = [root]
        left = True
        while queue:
            if left:
                ret.append([i.val for i in queue])
            else:
                ret.append([i.val for i in queue[::-1]])
            left = not left
            lenq = len(queue)
            for i in range(lenq):
                if queue[i].left:
                    queue.append(queue[i].left)
                if queue[i].right:
                    queue.append(queue[i].right)
            queue = queue[lenq:]
        return ret
