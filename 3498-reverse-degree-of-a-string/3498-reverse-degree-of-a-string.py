class Solution:
    def reverseDegree(self, s: str) -> int:
        mul = 1
        sum = 0 
        for i in range(len(s)):
            x = 123 -ord(s[i])
            mul = x*(i+1)
            sum = sum + mul 
        return sum
        
        