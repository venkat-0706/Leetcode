class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * len(text1)
        longest = 0

        for c in text2:
            cur_length = 0
            for i, val in enumerate(dp):
                if cur_length < val:
                    cur_length = val
                elif c == text1[i]:
                    dp[i] = cur_length + 1
                    longest = max(longest, cur_length + 1)
        
        return longest