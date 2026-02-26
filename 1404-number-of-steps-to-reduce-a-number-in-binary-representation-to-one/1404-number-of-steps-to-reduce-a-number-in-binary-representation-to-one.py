class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0 
        carry = 0 
        for i in range(len(s)-1,0,-1):
            bit = ord(s[i])&1
            steps += 1+(bit^carry)
            carry |= bit 
        return steps+carry
        