class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        link = [0] * n
        stk = res = []

        for i, c in enumerate(s):
            if c == '(':
                stk.append(i)
            elif c == ')':
                j = stk.pop()
                link[i] = j
                link[j] = i

        dr, i = 1, 0
        while i < n:
            if s[i] >= 'a':
                res.append(s[i])
            else:
                i = link[i]
                dr = -dr

            i += dr

        return ''.join(res)