class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """        
        r = s[::-1]
        i = len(s)
        while s[:i] != r[len(s) - i :]:
            i-=1
        return r[:len(s)-i] + s
