class Solution:
    def reverse(self, x: int) -> int:
        temp = abs(x) 
        rev = 0 
        while temp > 0 :
            rem = temp%10 
            rev = rev*10 + rem 
            temp //= 10 
        rev = rev if x>=0  else -rev 
        if rev < -2**31 or rev > 2**31-1:
            return 0 
        return rev


        