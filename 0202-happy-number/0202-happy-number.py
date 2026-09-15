class Solution:
    def getNext(self, n: int)-> int : 
        total = 0 
        while n > 0 : 
            digit = n % 10 
            total += digit * digit 
            n = n // 10 
        return total 
    def isHappy(self, n: int) -> bool: 
        slow = n 
        fast = self.getNext(n)
        while fast != 1 and slow != fast : 
            slow = self.getNext(slow)
            fast = self.getNext(self.getNext(fast))
        return fast == 1
        
         
        
        