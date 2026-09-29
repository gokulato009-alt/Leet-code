class Solution(object):
    def isAnagram(self, s, t):
        # d={}
        # d1={}
        # for i in s:
        #     if i  not in d:
        #         d[i]=s.count(i)
        
        # for i in t:
        #     if i  not in d1:
        #         d1[i]=s.count(i)

        # return d==d1
        # If lengths are different, they cannot be anagrams
        if len(s) != len(t):
            return False
            
        d = {}
        d1 = {}
        
        # Build frequency map for string s
        for char in s:
            if char not in d:
                d[char] = s.count(char)
                
        # Build frequency map for string t
        for char in t:
            if char not in d1:
                d1[char] = t.count(char)
                
        # The dictionaries must be identical for it to be an anagram
        return d == d1