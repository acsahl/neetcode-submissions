class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def sort(value):
            i = len(stones)-1
            while(i > 0):
                if value > stones[i]:
                    stones.insert(i+1,value)
                    return 
                else:
                    i -= 1
            stones.insert(0,value)
          
        stones.sort()
        while(len(stones) > 1):
            max1 = stones.pop(-1)
            max2 = stones.pop(-1)
            if max1 == max2:
                continue
            else:
                if max1 < max2:
                    max2 = max2 - max1
                    sort(max2)
                else:
                    max1 = max1-max2
                    sort(max1)
        if len(stones) == 1:
            return stones[0]
        else:
            return 0

            
        