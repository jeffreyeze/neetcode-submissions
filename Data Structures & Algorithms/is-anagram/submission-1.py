class Solution(object):
    def isAnagram(self, s, t):
        counts = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            counts[s[i]] = counts.get(s[i], 0) + 1
        for i in range(len(t)):
            counts[t[i]] = counts.get(t[i], 0) - 1
            if counts[t[i]] < 0:
                return False
        return True

"""
from collections import Counter

def isAnagram(self, s, t):
    return Counter(s) == Counter(t)
"""