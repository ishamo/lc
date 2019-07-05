class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lenn = len(height)
        if not height or lenn < 2: return 0

        l, r = 0, lenn-1
        mx_water = 0
        while l < r:
            area = (r - l) * min(height[r], height[l])
            if area > mx_water:
                mx_water = area

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return mx_water


        
