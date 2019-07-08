# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # iterable
        result = []
        if not root: return result

        stack = [root]
        visited = set()
        while stack:
            current = stack[-1]
            if current.left and current.left not in visited:
                current = current.left
                stack.append(current)
                continue

            result.append(current.val)
            visited.add(current)
            stack.pop(-1)

            if current.right:
                current = current.right
                stack.append(current)
                continue

        return result
#
#
# n1 = TreeNode(1)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n4 = TreeNode(4)
# n5 = TreeNode(5)
#
# n1.left, n1.right = n2, n3
# n2.left, n2.right = n4, n5
# s = Solution()
# print s.inorderTraversal(n1)
