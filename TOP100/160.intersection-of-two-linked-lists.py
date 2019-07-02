# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: return None

        p1 = headA
        p2 = headB

        while p1 and p2:
            p1 = p1.next
            p2 = p2.next

        s1, s2 = headA, headB
        while p1:
            p1 = p1.next
            s1 = s1.next

        while p2:
            p2 = p2.next
            s2 = s2.next

        while s1 != s2:
            s1 = s1.next
            s2 = s2.next

        return s1
