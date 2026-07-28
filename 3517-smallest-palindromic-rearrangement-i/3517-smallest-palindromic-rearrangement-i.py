from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        count = Counter(s)

        first = ""
        mid = ""

        for ch in sorted(count):
            first += ch * (count[ch] // 2)
            if count[ch] % 2:
                mid = ch

        second = first[::-1]

        return first + mid + second