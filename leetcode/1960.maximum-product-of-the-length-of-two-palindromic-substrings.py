#
# @lc app=leetcode id=1960 lang=python3
#
# [1960] Maximum Product of the Length of Two Palindromic Substrings
#

# @lc code=start
class Solution:
    def maxProduct(self, s: str) -> int:
        i = 0
        ans = []
        while(i < len(s)):
            pali = find_pali(s,i,j = i)
            print(pali)
            ans.append(pali)
            i += 1
        print("kam_khatam")
        i,j = 0,1
        while(j < len(s)):
            if s[i] == s[j]:
                print(i,j)
                pali = find_pali(s,i,j)
                print(pali)
                ans.append(pali)
            i += 1
            j += 1
        print(ans)
        ans.sort()
        return ans[-2]*ans[-1]
def find_pali(s,i,j):
    while(i > 0 and j < len(s) - 1 and s[i - 1] == s[j + 1]):
        i -= 1
        j += 1
    print(i,j,s[i:j+1])
    return j - i + 1        
# @lc code=end

