class Solution(object):
    def mergeAlternately(self, word1, word2):
        s = []
        for a in range(max(len(word1), len(word2))):
            if a < len(word1):
                s.append(word1[a])
            if a < len(word2):
                s.append(word2[a])
        return "".join(s)