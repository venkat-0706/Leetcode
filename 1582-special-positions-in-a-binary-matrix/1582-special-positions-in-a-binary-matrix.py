class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def check1(row):
            ans =[]
            for i,x in enumerate(row):
                if x == 1:
                    ans.append(i)
            return ans
        m = len(mat)
        n = len(mat[0])
        ans =0 
        col = [False]*n
        for row in mat:
            idx = check1(row)
            if len(idx)==1 and not col[j:=idx[0]]:
                col[j]=True
                count_col1=0
                for k in range(m):
                    count_col1+=mat[k][j]
                if count_col1==1:
                    ans+=1
            else:
                for j in idx:
                    col[j]==True
        return ans