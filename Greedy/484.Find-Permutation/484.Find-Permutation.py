class Solution:
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        s = s[0]+s
        nums = list(range(1,len(s)+1))
        i = 0
        result = []
        while i<len(s):
            j=i
            while (j<len(s) and s[j]==s[i]):
                j+=1
            if s[i]=='I':
                result+=nums[:j-i]
            else:
                result+=nums[:j-i][::-1]
                if i >= 1:
                    temp = result[i-1]
                    result[i-1:j-1] = result[i:j]
                    result[j-1] = temp
            nums = nums[j-i:]
            i=j
        return result
            
