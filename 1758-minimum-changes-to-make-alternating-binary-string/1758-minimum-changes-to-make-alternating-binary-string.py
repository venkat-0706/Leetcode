class Solution:
    def minOperations(self, s: str) -> int:
        left ,right = 0,0
        for i in range(len(s)):
            if i&1 == 0:
                if s[i] =="0":
                    right += 1
                else:
                    left += 1
            else:
                if s[i] == "1":
                    right += 1
                else:
                    left += 1
        return min(left,right)
        