class Solution:
    def binaryGap(self, n: int) -> int:
        max_dist = 0
        curr , prev = 0 , 0
        binary = bin(n)[2:]
        while curr != len(binary):
            if binary[curr] == '1':
                max_dist = max(max_dist , curr-prev)
                prev = curr 
            curr += 1
        return max_dist

        