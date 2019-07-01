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

        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        slow.next = None
        priv, cur = None, second
        while cur:
            cur.next, cur, priv = priv, cur.next, cur

        p = head
        while priv and p:
            if not priv.val == p.val: return False
            priv = priv.next
            p = p.next

        return True
