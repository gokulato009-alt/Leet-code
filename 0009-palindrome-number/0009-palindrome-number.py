class Solution(object):
    def isPalindrome(self, x):
        y= int(str(abs(x))[::-1])
        if y<2**31 and y>=-2**31 and x==y:
            return True
        else:
            return False    