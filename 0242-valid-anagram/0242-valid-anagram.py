class Solution(object):
    def isAnagram(self, s, t):
        d={}
        d1={}
        for i in s:
            if i not in d:
                d[i]=s.count(i)
        
        for i in t:
            if i not in d1:
                d1[i]=t.count(i)

        return d==d1
        
        