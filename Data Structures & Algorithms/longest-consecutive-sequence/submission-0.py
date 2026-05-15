class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestNum = 0
        for num in nums:
            seq = 1
            temp = num
            keepGoing = True
            while keepGoing:
                temp = temp + 1
                if temp in nums:
                    seq += 1
                else:
                    keepGoing = False
            if seq > longestNum:
                longestNum = seq
        return longestNum
        