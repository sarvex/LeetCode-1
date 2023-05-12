class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        Map = {w: i for i, w in enumerate(words)}
        words = sorted(words,key = lambda i:len(i))  

        result = []
        Set = set()
        for w in words:
            for L in range(len(w)+1):
                if w[:L] == w[:L][::-1] and w[L:][::-1] in Set:                    
                    result.append([Map[w[L:][::-1]],Map[w]])
                if w[L:] == w[L:][::-1] and w[:L][::-1] in Set:
                    result.append([Map[w], Map[w[:L][::-1]]])
            Set.add(w)
        return result                
