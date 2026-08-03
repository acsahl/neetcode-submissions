class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            index = gifts.index(max(gifts))
            gifts[index] = floor(sqrt(gifts[index]))
        return sum(gifts)