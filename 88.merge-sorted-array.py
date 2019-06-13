#coding: utf-8
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:m+n] = nums2
        nums1[:m+n] = sorted(nums1[:m+n])




# ✘ Wrong Answer
# ✘ 20/59 cases passed (N/A)
# ✘ testcase: '[4,5,6,0,0,0]\n3\n[1,2,3]\n3'
# ✘ answer: [2,3,1,4,5,6]
# ✘ expected_answer: [1,2,3,4,5,6]
