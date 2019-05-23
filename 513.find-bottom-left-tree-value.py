# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [(root, 1)]
        while queue:
            lenq = len(queue)
            for node in queue[:lenq]:
                if node[0].left:
                    queue.append((node[0].left, 1))
                if node[0].right:
                    queue.append((node[0].right, 0))

            if len(queue) == lenq:
                for item in queue:
                    if item[1]:
                        return item[0].val

                return queue[0][0].val

            else:
                queue = queue[lenq:]

        return -1
#
#
# n1 = TreeNode(1)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n4 = TreeNode(4)
# n5 = TreeNode(5)
# n6 = TreeNode(6)
# n7 = TreeNode(7)
#
# n1.left, n1.right = n2, n3
# n2.left = n4
# n3.left, n3.right = n5, n6
# n5.left = n7
#
# n1 = TreeNode(1)
# n2 = TreeNode(1)
# n1.right = n2
#
# s = Solution()
# print s.findBottomLeftValue(n1)
