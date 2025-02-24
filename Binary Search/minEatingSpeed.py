import math
# class Solution:
def minEatingSpeed(piles, h):
    # given k, total hr to eat all bananas = sum(math.ceil(piles[i]/k))
        # use binsearch: 
        # sort by ascending order
        # if actual_hr <= h: move left
        # elif actual_hr > h: move right
        
        left = 1
        right = max(piles)

        # use bin search from 0 to the max val to find k
        while left <= right:
            mid = (right + left) // 2

            # calculate the total hr
            actual_hr = 0
            for pile in piles:
                actual_hr += math.ceil(pile/mid)
            
            if actual_hr <= h:
                right = mid - 1
            else: left = mid + 1

        return left
    

piles=[332484035,524908576,855865114,632922376,222257295,690155293,112677673,679580077,337406589,290818316,877337160,901728858,679284947,688210097,692137887,718203285,629455728,941802184]
h=823855818
minEatingSpeed(piles, h)