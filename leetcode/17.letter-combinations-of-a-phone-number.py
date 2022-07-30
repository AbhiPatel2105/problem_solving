#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        data = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r','s'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }
        ans = [""]
        for i in range(len(digits)):
            len_ans = len(ans)
            for j in range(len_ans):
                temp = ans[j]
                for le in data[int(digits[i])]:
                    ans.append(temp + le)
                    # print(ans)
                    # print(le)
                    # temp = copy.deepcopy(ans[j])
                    # temp.append(le)
                    # ans.append(temp)
            for j in range(len_ans):
                ans.remove(ans[0])
                # print(ans)
        return ans
                    
        
# @lc code=end

