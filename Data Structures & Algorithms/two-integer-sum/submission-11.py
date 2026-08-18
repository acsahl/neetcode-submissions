class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        # {3:0,4:1,5:2,6:3}
        # {3:0}
        for i,num in enumerate(nums):
            comp = target - num
            
            if comp in seen:
                return [seen[comp],i]
            seen[num] = i

        