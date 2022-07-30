#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution(object):
    def minEatingSpeed(self, piles, h):
        low,high =  1,max(piles)
        speed = high
        while(low <= high):
            mid = (low + high)//2
            count = 0
            for ele in piles:
                count += ele // mid
                if ele % mid != 0:
                    count +=1
            if count <= h:
                speed = min(mid,speed)
                high = mid - 1
            else:
                low = mid + 1
        return speed
# @lc code=end

