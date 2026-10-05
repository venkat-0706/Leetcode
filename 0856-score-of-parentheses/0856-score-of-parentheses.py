class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = [0]
        for c in s : 
            if c == '(' :
                st.append(0)
            else  :
                current = st.pop()
                st[-1] += max(1,2*current)
        return st[0]
        

        