class Solution(object):
    def containsDuplicate(self, nums):
        if len(nums)==len(set(nums)):
            return False
        else:
            return True