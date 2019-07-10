# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        if not head.next: return None
        if head.next == head: return head
        if not head.next.next: return None

        fast, slow = head, head
        has_cycle = False
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                has_cycle = True
                break

        if not has_cycle: return None

        p = head
        while True:
            if p == fast: return p

            cp = fast.next
            while cp != fast:
                if cp == p: return p
                cp = cp.next

            p = p.next
#
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
# n5.next = None
# s = Solution()
# p = s.detectCycle(n1)
# print p
