class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            n=target-nums[i]
            if n in nums and nums.index(n)!=i:
                return [i,nums.index(n)]