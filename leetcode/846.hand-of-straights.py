#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#

# @lc code=start
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        a = len(hand)//groupSize
        print(hand)
        for i in range(a):
            print(i)
            print(hand[(i + 1)*groupSize - 1])
            print(hand[i*groupSize])
            print(hand[(i + 1)*groupSize - 1] - hand[i*groupSize])
            if hand[(i + 1)*groupSize - 1] - hand[i*groupSize] ==  groupSize - 1:
                continue
            else:
                return False
        return True
# @lc code=end

