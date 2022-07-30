#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        mask = 1
        ans = ''
        for i in range(32):
            temp = n & mask
            if temp == 0:
                ans += '0'
            else:
                ans += '1'
            mask = mask << 1
        ans = '0b' + ans
        return int(ans,base=2)
# @lc code=end

