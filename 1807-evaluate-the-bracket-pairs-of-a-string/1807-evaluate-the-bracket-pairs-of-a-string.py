class Solution:
    def evaluate(self, s: str, K: List[List[str]]) -> str:
        d = dict(K)
        res, i = [], 0

        while i < len(s):
            if s[i] == '(':
                j = s.find(')', i + 1)
                res.append(d.get(s[i + 1:j], '?'))
                i = j
            else:
                res.append(s[i])
            i += 1

        return "".join(res)