#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_dict = {}
        for i in range(len(s1)):    
            s1_dict[s1[i]] = 1 + s1_dict.get(s1[i],0)
        l,r = 0,len(s1)
        s2_dict = {}
        for i in range(len(s1)):    
            s2_dict[s2[i]] = 1 + s2_dict.get(s2[i],0)
        if s1_dict == s2_dict:
            return True 
        while(r < len(s2)):
            s2_dict[s2[r]] = 1 + s2_dict.get(s2[r],0)
            s2_dict[s2[l]] -= 1
            if s2_dict[s2[l]] == 0:
                s2_dict.pop(s2[l])
            r += 1
            l += 1
            if s1_dict ==  s2_dict:
                return True
        return False
# @lc code=end

