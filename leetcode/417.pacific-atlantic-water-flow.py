#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visited = []
        pacific = []
        atlantic = []
        for i in range(len(heights)):
            visited.append([0]*len(heights[0]))
            pacific.append([0]*len(heights[0]))
            atlantic.append([0]*len(heights[0]))
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if visited[i][j] != 1:
                    visited,pacific = pacific_function(visited,pacific,heights,i,j)
        print(pacific)
        for i in range(len(heights)-1,-1,-1):
            for j in range(len(heights[0])-1,-1,-1):
                if visited[i][j] != 0:
                    visited,atlantic = atlantic_function(visited,atlantic,heights,i,j)
        print(atlantic)
        ans = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if atlantic[i][j] == 1 and pacific[i][j] == 1:
                    ans.append([i,j])
        return ans        
                    
def pacific_function(visited,pacific,heights,i,j):
    visited[i][j] = 1
    if i == 0 or j==0:
        pacific[i][j] = 1
        return visited,pacific
    temp = [[-1,0],[0,-1],[1,0],[0,1]]
    for ele in temp:
        temp_i = i + ele[0]
        temp_j = j + ele[1]
        if temp_i >= 0 and temp_i < len(heights) and temp_j >= 0 and temp_j < len(heights[0]):
            if pacific[temp_i][temp_j] == 1 and heights[temp_i][temp_j] <= heights[i][j]:
                pacific[i][j] = 1
                return visited,pacific
            if visited[temp_i][temp_j] != 1 and heights[temp_i][temp_j] <= heights[i][j]:
                visited,pacific = pacific_function(visited,pacific,heights,temp_i,temp_j)
    return visited,pacific

def atlantic_function(visited,atlantic,heights,i,j):
    visited[i][j] = 0
    if i == len(heights) - 1 or j == len(heights[0]) - 1:
        atlantic[i][j] = 1
        return visited,atlantic
    temp = [[1,0],[0,1],[0,-1],[-1,0]]
    for ele in temp:
        temp_i = i + ele[0]
        temp_j = j + ele[1]
        if temp_i >= 0 and temp_i < len(heights) and temp_j >= 0 and temp_j < len(heights[0]):
            if atlantic[temp_i][temp_j] == 1 and heights[temp_i][temp_j] <= heights[i][j]:
                atlantic[i][j] = 1
                return visited,atlantic
            if visited[temp_i][temp_j] != 0 and heights[temp_i][temp_j] <= heights[i][j]:
                visited,atlantic = atlantic_function(visited,atlantic,heights,temp_i,temp_j)
    return visited,atlantic
            
# @lc code=end

