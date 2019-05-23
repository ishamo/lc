# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return self.val

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if not root: return result

        queue = [root]

        while queue:
            result.append(max([i.val for i in queue]))
            lenq = len(queue)
            # print(queue)
            for node in queue[:lenq]:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            queue = queue[lenq:]

        return result
#
#
#
# n1 = TreeNode(1)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n4 = TreeNode(5)
# n5 = TreeNode(3)
# n6 = TreeNode(9)
#
# n1.left = n3
# n1.right = n2
# n3.left = n4
# n3.right = n5
# n2.right = n6
#
#
# s = Solution()
# print s.largestValues(n1)
