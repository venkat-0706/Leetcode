class Solution:
    def checkValidString(self, s: str) -> bool:
        l = h = 0

        for c in s:
            l += ((c == '(') << 1) - 1
            h += ((c != ')') << 1) - 1

            if h < 0: return False

            l = max(l, 0)

        return l == 0