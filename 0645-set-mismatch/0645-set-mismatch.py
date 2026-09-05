class Solution(object):
    def findErrorNums(self, nums):
        seen = set()
        d = 0

        for num in nums:
            if num in seen:
                d = num
            seen.add(num)

        m = 0
        for i in range(1, len(nums) + 1):
            if i not in seen:
                m = i

        return [d, m]
            
        