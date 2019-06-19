# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#     def __repr__(self):
#         return str(self.val)
#
#     def __str__(self):
#         return self.__repr__()

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head

        prev, cur = None, head
        while cur:
            # this is wrong, why?
            # prev, cur, cur.next = cur, cur.next, prev
            # that is right.
            cur.next, cur, prev = prev, cur.next, cur

        return prev


#
# n1 = ListNode(1)
# n2 = ListNode(2)
# n3 = ListNode(3)
# n4 = ListNode(4)
# n5 = ListNode(5)
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
#
# s = Solution()
# p = s.reverseList(n1)
# while p:
#     print p.val
#     p = p.next
