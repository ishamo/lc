# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next: return head
        p = head
        length = 0
        while p:
            length += 1
            p = p.next

        k = k % length

        for i in range(k):
            head = self.rotateOneStep(head)

        return head

    def rotateOneStep(self, head):
        if not head or not head.next: return head
        p = head
        cur = head
        while p.next:
            cur = p
            p = p.next

        p.next = head
        cur.next = None

        return p


# [1,2,3], 2000000000
#
#
# #################################
# n1 = ListNode(1)
# n2 = ListNode(2)
# n3 = ListNode(3)
# n4 = ListNode(4)
# n5 = ListNode(5)
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# head = n1
# s = Solution()
# head = s.rotateRight(head, 2)
# print head.val
# print head.next.val
# print head.next.next.val
# print head.next.next.next.val
# print head.next.next.next.next.val
#
