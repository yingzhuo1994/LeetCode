# 1st solution
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        nb_swap = 0
        place = {x:i for (i,x) in enumerate(row)}
        for i in range(len(row)):
            x = row[i]
            
            # find y partner of x :
            if x % 2 == 0:
                y = x + 1
            else:
                y = x - 1
            j = place[y]
            
            # if need a swap
            if abs(i-j) > 1: 
                row[i+1], row[j] = row[j], row[i+1]
                place[row[i+1]] = i+1
                place[row[j]] = j
                nb_swap += 1
                
        return nb_swap
        