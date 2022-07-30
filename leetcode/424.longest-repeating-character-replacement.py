#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        temp = {}
        l,r = 0,0
        res = 0
        window_size = 0
        max_ele = 0
        while(l < len(s) and r < len(s)):
            if s[r] not in temp:
                temp[s[r]] = 1
            else:
                temp[s[r]] += 1
            if temp[s[r]] >= max_ele:
                max_ele = temp[s[r]]
            r += 1
            window_size = r - l
            if window_size - max_ele <= k:
                res = max(res,window_size)
            else:
                temp[s[l]] -= 1
                l += 1
        return res
# @lc code=end

