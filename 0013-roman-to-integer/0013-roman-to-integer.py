class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            "M" : 1000,
            "D" : 500,
            "C" : 100,
            "L" : 50,
            "X" : 10,
            "V" : 5,
            "I" :1
        }
        num = 0
        for i in range(0,len(s)):
            if (i+1 < len(s) and dict[s[i]] < dict[s[i+1]]):
                num = num - dict[s[i]]
            else:
                num = num + dict[s[i]]
        return num