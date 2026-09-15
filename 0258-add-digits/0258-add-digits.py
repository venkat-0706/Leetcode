class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0 :
            return num 
        while num >= 10 : 
            total =  0 
            while num != 0 :
                digit =  num % 10 
                total += digit 
                num = num // 10 
            num = total 
        return num

        