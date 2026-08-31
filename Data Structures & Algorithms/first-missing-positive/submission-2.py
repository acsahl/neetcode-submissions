class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        maxi = max(nums)
        for i in range(1,maxi):
            if i not in nums:
                return i
        if maxi <= 0:
            return 1
        else:
            return maxi + 1

        