class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # could've just used a regular counter 
        # also didnt need to count twenties but prolly useful for a legit bank idk
        bank = {5:0,10:0,20:0}
        for bill in bills:
            if bill == 5:
                bank[5] += 1
            else:
                change = bill - 5
                if change == 5:
                    if bank[5] == 0:
                        return False
                    else:
                        bank[5] -= 1
                        bank[10] += 1
                elif change == 15:
                    if bank[10] > 0 and bank[5] > 0:
                        bank[10] -= 1
                        bank[5] -= 1
                        bank[20] += 1
                    elif bank[5] >= 3:
                        bank[5] -= 3
                        bank[20] += 1
                    else:
                        return False
        return True

        