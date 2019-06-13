class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False

        rows, cols = len(matrix), len(matrix[0])

        if matrix[0][0] > target or matrix[-1][-1] < target: return False

        l, r = 0, rows-1
        locate_row, locate_col = -1, -1
        while l <= r:
            mid = (l + r) / 2
            # print('matrix[mid][-1]', matrix[mid][-1])
            if matrix[mid][-1] == target: return True
            elif matrix[mid][-1] > target:
                # print(11111)
                if mid == 0 or matrix[mid-1][-1] < target:
                    locate_row = mid
                    break
                else:
                    r = mid - 1
            else:
                # print(2222)
                if matrix[mid+1][-1] > target:
                    locate_row = mid+1
                    break
                else:
                    l = mid + 1

        l, r = 0, cols-1

        # print('locate_row', locate_row)
        while l <= r:
            mid = (l + r) / 2
            if matrix[locate_row][mid] == target: return True
            elif matrix[locate_row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False
#
#
# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
#
# s = Solution()
# print s.searchMatrix(matrix, 3)

