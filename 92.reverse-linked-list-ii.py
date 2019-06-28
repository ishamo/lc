# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or m >= n: return head
        if m <= 0 or n <= 0: return head
        if m == 1:
            print(11111111111)
            p1 = head
            priv = None
            while p1 and m <= n:
                print(22222222222)
                p1.next, p1, priv = priv, p1.next, p1
                m += 1
            if p1:
                head.next = p1
            return priv

        start = 0
        first = head
        while start < m-2:
            first = first.next
            start += 1
            if not first: return head

        second = first.next
        tail = second
        priv = None
        # start += 1
        # print('start', start)
        while second and start < n-1:
            second.next, second, priv = priv, second.next, second
            start += 1
            # print('2start', start)
        first.next = priv
        if second:
            tail.next = second
        return head
#
# n1 = ListNode(3)
# n2 = ListNode(5)
# n1.next = n2
# s = Solution()
# head = s.reverseBetween(n1, 1, 2)
# print head.val
# print head.next.val
# print head.next.next
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
# S = Solution()
# head = S.reverseBetween(n1, 2, 4)
# print head.val
# print head.next.val
# print head.next.next.val
# print head.next.next.next.val
# print head.next.next.next.next.val
# print head.next.next.next.next.next.val
# print head.next.next.next.next.next.next
#
#
# 1 -> 2 -> 3 -> 4 -> 5
# 1 -> 5 -> 4 -> 3 -> 2
# 1 -> 4 -> 3 -> 2 -> 5 -> 6
