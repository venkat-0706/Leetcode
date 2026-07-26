class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xor = 0 
        for ch in s:
            xor = xor^ ord(ch)
        
        for ch in t:
            xor = xor^ord(ch)

        return chr(xor)