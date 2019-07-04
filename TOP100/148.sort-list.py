# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head

        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        slow.next = None
        first = head
        l1 = self.sortList(first)
        l2 = self.sortList(second)
        l = self.mergeList(l1, l2)
        return l

    def mergeList(self, l1, l2):
        priv = ListNode(-1)
        p = priv
        while l1 and l2:
            if l1.val <= l2.val:
                priv.next = l1
                l1 = l1.next
            else:
                priv.next = l2
                l2 = l2.next

            priv = priv.next

        if l1:
            priv.next = l1
        if l2:
            priv.next = l2
        return p.next
