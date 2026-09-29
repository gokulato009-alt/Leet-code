class Solution(object):
    def isAnagram(self, s, t):
        # d={}
        # d1={}
        # for i in s:
        #     if i not in d:
        #         d[i]=s.count(i)
        
        # for i in t:
        #     if i not in d1:
        #         d1[i]=t.count(i)

        # return d==d1

        if len(s) != len(t):
            return False
            
        d = {}
        d1 = {}
        for char in s:
            if char not in d:
                d[char] = s.count(char)
        for char in t:
            if char not in d1:
                d1[char] = t.count(char)

        return d == d1
        
        