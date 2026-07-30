class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        count = 0 
        for i in range(n):
            count += (i//8) + 1 
        return count
        
        