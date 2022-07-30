#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # def any(word,arr):
        #     if len(word) == 0:
        #         return True
        #     for i in range(len(word)):
        #         for w in arr:
        #             if i + len(w) <= len(word) and word[i:i+len(w)] == w:
        #                 ans = any(word[0:i],arr)
        #                 if ans:
        #                     return True
        #         # temp = word[i] + temp
        #         # if temp in arr:
        #         #     ans = any(word[0:i],arr)
        #         #     if ans:
        #         #         return True
        #     return False
        # return any(s,wordDict)
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        
        return dp[0]
# @lc code=end

