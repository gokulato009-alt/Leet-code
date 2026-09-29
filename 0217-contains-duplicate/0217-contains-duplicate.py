class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))

        # if len(nums)==len(set(nums)):
        #     return False
        # else:
        #     return True


# class Solution(object):
#     def containsDuplicate(self, nums):
#         a=set()
#         for i in nums:
#             if i in a:
#                 return True
#             else:
#                 a.add(i)
#         return Falsej