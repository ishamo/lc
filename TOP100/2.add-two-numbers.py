# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1: return l2
        if not l2: return l1

        head = ListNode(-1)
        p = head

        c = 0
        while l1 and l2:
            sm = c + l1.val + l2.val
            value = sm % 10
            c = sm / 10
            p.next = ListNode(value)
            l1 = l1.next
            l2 = l2.next
            p = p.next

        l = l1 or l2
        while l:
            sm = c + l.val
            value = sm % 10
            c = sm / 10
            p.next = ListNode(value)
            p = p.next
            l = l.next

        if c:
            p.next = ListNode(c)

        return head.next
