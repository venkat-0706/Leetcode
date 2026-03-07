class Solution:
    def minFlips(self, s: str) -> int:

        n, list0, list1, s, ans = len(s), [0,0], [0,0], list(map(int,s)), inf
       
        for i,digit in enumerate(s):
            list0[(i&1)^(digit)]+= 1

        if not n%2: return min(list0)

        for i,digit in enumerate(s):
            list0[ i&1^digit]-= 1
            list1[~i&1^digit]+= 1
            
            ans = min(ans,list0[0]+list1[0],list0[1]+list1[1])

        return ans