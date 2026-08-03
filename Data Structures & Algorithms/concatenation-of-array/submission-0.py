class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        fin = [0] * (2 * n)
        for i in range(n):
            fin[i] = nums[i]
            fin[i+n] = nums[i]
        return fin
        