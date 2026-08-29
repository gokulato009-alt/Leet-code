class Solution(object):
    def getConcatenation(self, nums):
        ans=[]
        n=len(nums)
        for i in range(n):
            ans.append(nums[i])
        for i in range(n):
            ans.append(nums[i])
        
        return ans
            
        