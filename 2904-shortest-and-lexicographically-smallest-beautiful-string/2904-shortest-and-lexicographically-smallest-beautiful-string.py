class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        for m in range(k, n + 1):
            ans = ""
            for i in range(m, n + 1):
                t = s[i - m : i]
                if (not ans or t < ans) and t.count("1") == k:
                    ans = t
            if ans:
                return ans
        return ""