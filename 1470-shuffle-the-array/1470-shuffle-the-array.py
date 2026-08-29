class Solution(object):
    def shuffle(self, l, n):
        a=[]
        for i in range(n):
            a.append(l[i])
            a.append(l[i+n])

        return a