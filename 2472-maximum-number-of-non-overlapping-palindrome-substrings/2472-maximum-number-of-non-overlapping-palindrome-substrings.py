class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        intervals = []
        
        for center in range(2 * n - 1):
            l = center // 2
            r = l + (center % 2)
            
            while l >= 0 and r < n and s[l] == s[r]:
                length = r - l + 1
                if length == k or length == k + 1:
                    intervals.append((l, r))
                    break  
                l -= 1
                r += 1
                
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        last_end = -1
        
        for l, r in intervals:
            if l > last_end:
                count += 1
                last_end = r
                
        return count