# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#     def __str__(self):
#         p = self
#         value = []
#         while p:
#             value.append(p.val)
#             p = p.next
#         return str(value)

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

        l1 = self.sortList(head)
        l2 = self.sortList(second)
        return self.mergeList(l1, l2)

    def mergeList(self, l1, l2):
        head = ListNode(-1)
        p = head
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next

            p = p.next

        if l1:
            p.next = l1
        if l2:
            p.next = l2

        return head.next
#
#
# l1 = ListNode(4)
# l2 = ListNode(2)
# l3 = ListNode(1)
# l4 = ListNode(3)
# l1.next = l2
# l2.next = l3
# l3.next = l4
# s = Solution()
# h = s.sortList(l1)
# print h.val
# print h.next.val
# print h.next.next.val
# print h.next.next.next.val
# print h.next.next.next.next
