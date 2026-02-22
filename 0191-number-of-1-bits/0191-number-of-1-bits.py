class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0 
        binary = bin(n)[2:]
        curr = 0
        while curr < len(binary):
            if binary[curr] == '1':
                count += 1
            curr += 1
        return count