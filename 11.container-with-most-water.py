class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        l, r = 0, length - 1
        water = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            if area > water: water = area
            mn = l if height[l] < height[r] else r
            if mn == l:
                l += 1
            else:
                r -= 1
        return water
