class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        freq = [0] * 52

        for i, (a, b) in enumerate(zip(s1, s2)):
            off = (i & 1) * 26
            freq[ord(a) - 97 + off] += 1
            freq[ord(b) - 97 + off] -= 1

        return all(c == 0 for c in freq)