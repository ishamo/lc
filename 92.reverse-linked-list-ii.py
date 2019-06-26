# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or m <= n: return head

        prev, cur = None, Head
        start, end = 0, 0
        while cur and start < m:


# 1 -> 2 -> 3 -> 4 -> 8 -> 7 -> 6 -> 5 -> 9 -> None
