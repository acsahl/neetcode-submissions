import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #finding max element is more efficient w heap
        #change all to negative to support maxheap
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while(len(stones) > 1):
            max1 = -heapq.heappop(stones)
            max2 = -heapq.heappop(stones)
            if max1 == max2:
                continue
            else:
                heapq.heappush(stones,-(max1-max2))
        if stones:
            return -stones[0]
        else:
            return 0
            
            
        