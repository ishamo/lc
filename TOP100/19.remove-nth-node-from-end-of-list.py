# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head: return head

        fast, slow = head, head
        count = 1
        while fast.next:
            fast = fast.next
            count += 1
            if count > n: break

        if count <= n: return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head
#
#
# n1 = ListNode(1)
# n2 = ListNode(2)
# n3 = ListNode(3)
# n4 = ListNode(4)
# n5 = ListNode(5)
# n6 = ListNode(6)
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n6
#
# s = Solution()
# head = s.removeNthFromEnd(n1, 2)
# p = head
# while p:
#     print p.val
#     p = p.next
#
