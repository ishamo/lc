# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_values, l2_values = [], []
        while l1:
            l1_values.append(l1.val)
            l1 = l1.next

        while l2:
            l2_values.append(l2.val)
            l2 = l2.next

        l1_values.extend(l2_values)
        l1_values.sort()

        len1 = len(l1_values)
        record, head = None, None
        for i in l1_values[::-1]:
            head = ListNode(i)
            head.next = record
            record = head

        return head


