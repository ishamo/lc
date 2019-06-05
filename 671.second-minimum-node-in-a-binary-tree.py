# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root or not root.left and not root.right: return -1

        queue = [root]

        mn = root.val
        bigint = 0xffffffff
        second = bigint

        while queue:
            lens = len(queue)
            for n in queue:
                if n.left: queue.append(n.left)
                if n.right: queue.append(n.right)

                collect = [item.val for item in queue[lens:] if item.val > mn]
                collect.sort()
                if collect and collect[0] < second:
                    second = collect[0]

            queue = queue[lens:]

        if second == bigint: return -1
        return second

#
#
#
#
#
#n1 = TreeNode(2)
#n2 = TreeNode(2)
#n3 = TreeNode(5)
#n4 = TreeNode(5)
#n5 = TreeNode(7)
#
#n1.left, n1.right = n2, n3
#n3.left, n3.right = n4, n5
#
#s = Solution()
#print  s.findSecondMinimumValue(n1)
#
#
#
#

# arr = [1,1,3,1,1,3,4,3,1,1,1,3,8,4,8,3,3,1,6,2,1]
