class Solution(object):
    def reverse(self, x):
        sign=-1 if x<0 else 1
        y=sign*int(str(abs(x))[::-1])

        if y>=(-2)**31 and y<2**31:
            return y
        else:
            return 0

        