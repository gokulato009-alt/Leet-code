class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        l = nums[:]
        l1 = nums[:]
        l.sort()
        for i in range(len(nums)):
            original_val = nums[i]
            smaller_count = l.index(original_val)
            l1[i] = smaller_count
            
        return l1
        
