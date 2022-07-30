#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        a = {}
        for word in words:
            if word in a:
                a[word] += 1
            else:
                a[word] = 1
        a = sorted(a.items(), key=lambda x:x[1],reverse=True)
        ans = []
        for i in range(k):
            ans.append(a[i][0])
        return ans
# @lc code=end

