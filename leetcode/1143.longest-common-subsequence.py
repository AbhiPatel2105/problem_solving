#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        temp = []
        for i in range(len(text2) + 1):
            temp.append([0]*(len(text1) + 1))
        for i in range(1,len(temp)):
            for j in range(1,len(temp[0])):
                if text1[j - 1] == text2[i - 1]:
                    temp[i][j] = temp[i - 1][j - 1] + 1
                else:
                    temp[i][j] = max(temp[i][j-1],temp[i - 1][j])
        return temp[len(temp) - 1][len(temp[0]) - 1]
# @lc code=end

