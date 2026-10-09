class Solution(object):
    def isPalindrome(self, s):
        cleaned = ""
        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()
        if cleaned != cleaned[::-1]:
            return False
        return True