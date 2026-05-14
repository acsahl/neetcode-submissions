class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zeroFlag = False
        zeroCount = 0
        for num in nums:
            if num == 0:
                zeroFlag = True
                zeroCount += 1
            else:
                total = num * total
        output_arr = []
        if zeroCount > 1:
            return [0] * len(nums)
        for num in nums:
            if zeroFlag:
                if num == 0:
                    output_arr.append(total)
                else:
                    output_arr.append(0)
            else:
                output_arr.append(int(total/num))
        return output_arr
        