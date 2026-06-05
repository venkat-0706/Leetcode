class Solution:
    def reverseWords(self, s: str) -> str:
        words =  s.split()
        res = []
        for i in range(len(words)-1,-1,-1):
            res.append(words[i])
            if i!=0:
                res.append(" ")
        return "".join(res)
        