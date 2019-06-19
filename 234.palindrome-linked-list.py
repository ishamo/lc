# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: return True

        lst = []
        p = head
        while p:
            lst.append(p.val)
            p = p.next

        lenn = len(lst)

        l, r = 0, lenn-1
        while l < r:
            if not lst[l] == lst[r]: return False

            l += 1
            r -= 1

        return True
