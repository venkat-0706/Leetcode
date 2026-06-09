class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(0 , len(s)):
            if s[i] == "(":
                stack.append(")")
            elif s[i] == "{":
                stack.append("}")
            elif s[i] == "[":
                stack.append("]")
            else:
                if len(stack) == 0  or stack.pop() != s[i]:
                    return False

        return len(stack) == 0
            
        