# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lists = filter(lambda x: bool(x), lists)
        if not lists: return None

        head = ListNode(-1)
        priv = head
        while True:
            record = 0
            for idx, l in enumerate(lists):
                if not priv.next or priv.next.val > l.val:
                    record = idx
                    priv.next = l

            priv = priv.next
            lists[record] = lists[record].next
            priv.next = None
            if not lists[record]:
                lists.pop(record)

            if not lists: break

        return head.next
#
#
# def make_list(arr):
#     if not arr: return None
#     head = ListNode(arr[0])
#     p = head
#     for i in range(1, len(arr)):
#         p.next = ListNode(arr[i])
#         p = p.next
#
#     return head
#
# h1 = make_list([1,4,5])
# h2 = make_list([1,3,4])
# h3 = make_list([2,6])
# s = Solution()
# print([h1, h2, h3])
# head = s.mergeKLists([h1,h2,h3])
# # print('head', head)
# pp = head
# while pp:
#     print pp.val
#     pp = pp.next
#
