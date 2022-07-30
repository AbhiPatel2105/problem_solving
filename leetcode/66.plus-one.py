#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] = digits[-1] + 1
        if digits[-1] > 9:
            carry = digits[-1]//10
            digits[-1] = digits[-1]%10
        else:
            carry = 0
        for i in range(len(digits)-2,-1,-1):
            sum = digits[i] + carry
            carry = sum//10
            digits[i] = sum%10
        if carry > 0:
            digits.insert(0, carry)
        return digits

# @lc code=end

