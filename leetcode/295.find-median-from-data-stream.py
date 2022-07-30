#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
class MedianFinder:

    def __init__(self):
        self.H = []

    def addNum(self, num: int) -> None:
        for i in range(len(self.H)):
            if self.H[i] <= num:
                continue
            self.H.insert(i,num)
            return
        self.H.append(num)
    def findMedian(self) -> float:
        
        if len(self.H) % 2 == 0:
            return (self.H[(len(self.H)//2)-1] + self.H[len(self.H)//2])/2
        else:
            return self.H[(len(self.H)//2)]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

