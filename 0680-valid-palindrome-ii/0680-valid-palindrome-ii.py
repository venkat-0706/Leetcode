class Solution:
    def ispalindrome(self,s,left,right):
        while left < right:
            if s[left]!= s[right]:
                return False 
            left += 1
            right -= 1 
        return True
    def validPalindrome(self, s: str) -> bool:
        i,j = 0, len(s)-1
        while i < j :
            if s[i]!= s[j]:
                return (self.ispalindrome(s,i,(j-1)) or self.ispalindrome(s,(i+1),j))
            i += 1
            j -= 1
        return True
        
        