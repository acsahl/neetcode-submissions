class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        final = []
        for i in range(1,len(nums)+1):
            if i not in nums:
                final.append(i)
        return final
        