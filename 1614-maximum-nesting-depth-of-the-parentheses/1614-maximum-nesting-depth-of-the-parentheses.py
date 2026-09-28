class Solution:
    def maxDepth(self, s):
        depth = 0
        r = 0
        for c in s:
            if c == ')':
                depth -= 1
                continue
            # Digits and operators
            if c != '(':
                continue
            depth += 1
            # New max only possible after '('
            if depth > r:
                r = depth
        return r