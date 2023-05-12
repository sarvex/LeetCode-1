class Solution:
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N==1: return 0
        a = self.kthGrammar(N-1,(K+1)//2)
        return 1 if a==1 and K%2==1 or a != 1 and K%2 != 1 else 0
