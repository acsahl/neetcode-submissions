class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqArr = {}
        final = []
        for num in nums:
            if num in freqArr:
                freqArr[num] += 1
            else:
                freqArr[num] = 1
        for i in range(k):
            maxKey = max(freqArr,key = freqArr.get)
            freqArr.pop(maxKey)
            final.append(maxKey)
        return final

