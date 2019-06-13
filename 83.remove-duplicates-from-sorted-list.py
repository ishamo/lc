# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        p, q = head, None

        while p:
            q = p.next
            while q and q.val == p.val:
                q = q.next

            p.next = q
            p = q

        return head
