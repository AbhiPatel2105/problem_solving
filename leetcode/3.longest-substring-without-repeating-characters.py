#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        i = 0
        while(i < len(s)):
            count = 0
            temp = {}
            j = i
            while(j < len(s) and s[j] not in temp):
                temp[s[j]] = j
                j += 1
                count += 1
            if j < len(s):
                i = temp[s[j]] + 1
            else:
                i = j
            ans = max(ans,count)
        return ans
# @lc code=end

