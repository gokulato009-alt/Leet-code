class Solution(object):
    def findMaxConsecutiveOnes(self, l):
        max_ones=0
        c=0
        for i in l:
            if i==1:
                c=c+1
                max_ones=max(max_ones,c)
            else:
                c=0
        return max_ones