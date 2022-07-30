#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        min_len = float("inf")
        ans = ""
        t_dict = {}
        for i in range(len(t)):    
            t_dict[t[i]] = 1 + t_dict.get(t[i],0)
        s_dict = {}
        for key in t_dict.keys():
            s_dict[key] = 0
        for i in range(len(t)):
            if s[i] in s_dict:
                s_dict[s[i]] += 1
        l,r = 0,len(t)
        print(r)
        if is_gre(s_dict,t_dict):
            return s[0:r]
        while(l < len(s) and r < len(s)):
            while(l < len(ans)):
                if s[l] not in s_dict:
                    l += 1
                else:
                    if s_dict[s[l]] > t_dict[s[l]]:
                        s_dict[s[l]] -= 1
                        l += 1
                    else:
                        break
            if s[r] in s_dict:
                s_dict[s[r]] += 1
                while(s[r] == s[l] and s_dict[s[r]] > t_dict[s[r]]):
                    s_dict[s[r]] -= 1
                    l += 1
                r += 1
                if is_gre(s_dict,t_dict) and r - l< min_len:
                    min_len = r - l
                    ans = s[l:r]
            else:
                r += 1
        while(l < len(s)):
            if s[l] not in s_dict:
                l += 1
            else:
                if s_dict[s[l]] > t_dict[s[l]]:
                    l += 1
                    s_dict[s[l]] -= 1
                else:
                    break
        if is_gre(s_dict,t_dict) and r - l< min_len:
            min_len = r - l
            ans = s[l:r]
            
        return ans
        

        
                    
                
                
                    
                    
                
def is_gre(s_dict,t_dict):
    for key in t_dict.keys():
        if s_dict[key] >= t_dict[key]:
            continue
        return False
    return True
# @lc code=end

