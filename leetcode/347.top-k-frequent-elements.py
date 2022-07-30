#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = Counter(nums)
        m = dict(sorted(m.items(), key=lambda item: item[1],reverse=True))
        ans = []
        for ele in m.keys():
            ans.append(ele)
            k -= 1
            if k == 0:
                return ans
                
# @lc code=end

