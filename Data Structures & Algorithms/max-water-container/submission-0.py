class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) -1 
        maxAmt = 0
        while (i < j):
            area = min(heights[i],heights[j]) * (j-i)
            if area > maxAmt:
                maxAmt = area
            if heights[i] > heights[j]:
                j -= 1
            elif heights[j] > heights[i]:
                i += 1
            else:
                i += 1
                j -= 1
        return maxAmt
        