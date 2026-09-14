class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp_num  = x 
        result = 0 
        while x >  0 :
            digit =  x % 10 
            result = result * 10 + digit
            x = x // 10 
        return temp_num == result 

        