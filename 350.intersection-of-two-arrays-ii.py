class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        if not nums1 or not nums2: return result
        len1 = len(nums1)
        pool = [0] * len1

        for i in nums2:
            for idx, j in enumerate(nums1):
                if i == j and not pool[idx]:
                    result.append(i)
                    pool[idx] = 1
                    break

        return result
