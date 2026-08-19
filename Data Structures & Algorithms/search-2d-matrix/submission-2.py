class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search 
        # flatten out into single long array 
        nr = len(matrix)
        nc = len(matrix[0])
        lo = 0
        hi = (nr * nc) - 1 
        while(lo <= hi):
            # account for overflow?
            mid = (lo + hi) // 2
            # cookie buckets 
            midVal = matrix[mid//nc][mid%nc]
            if (midVal == target):
                return True
            elif (midVal < target):
                lo = mid + 1
            else:
                hi = mid - 1 
        return False
        