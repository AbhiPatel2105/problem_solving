#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = ["("]
        no_of_open= [1]
        no_of_rem = [n - 1]
        inserted = True
        while(inserted):
            inserted = False
            len_ans = len(ans)
            f_ans = []
            f_no_open = []
            f_no_rem = []
            for i in range(len_ans):
                print(ans,i)
                if no_of_open[i] >= 1:
                    temp = ans[i] + ")"
                    inserted = True
                    f_ans.append(temp)
                    f_no_open.append(no_of_open[i] - 1)
                    f_no_rem.append(no_of_rem[i])
                # else:
                #     if no_of_rem[i] >= 1:
                #         temp = ans[i] + "("
                #         inserted = True
                #         ans.append(temp)
                #         no_of_open.append(no_of_open[i] + 1)
                #         no_of_rem.append(no_of_rem[i] - 1)
                if no_of_rem[i] >= 1:
                    temp = ans[i] + "("
                    inserted = True
                    f_ans.append(temp)
                    f_no_open.append(no_of_open[i] + 1)
                    f_no_rem.append(no_of_rem[i] - 1)
                print(ans)
                if inserted:
                    ans = copy.deepcopy(f_ans)
                    no_of_open = copy.deepcopy(f_no_open)
                    no_of_rem = copy.deepcopy(f_no_rem)
        return ans

                    
# @lc code=end

