class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        st = [-1]
        
        for i, c in enumerate(s):
            if c == '(':
                st.append(i)
            else:
                st.pop()
                
                if not st:
                    st.append(i)
                else:
                    res = max(res, i - st[-1])
                    
        return res