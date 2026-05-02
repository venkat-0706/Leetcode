class Solution:
    """My Recursive Memoization Digit DP Solution!!"""
    def rotatedDigits(self, n: int) -> int:
        invalid = {3, 4, 7}
        change = {2, 5, 6, 9}
        digits = list(map(int, str(n)))

        def dp(i, constrained, is_changed, memo):
            if i == len(digits):
                if is_changed:
                    return 1
                else:
                    return 0

            if not constrained:
                if (i, is_changed) not in memo:
                    memo[(i, is_changed)] = 0
                    for j in range(10):
                        if j in invalid:
                            continue
                        new_change = is_changed
                        if j in change:
                            new_change = True

                        memo[(i, is_changed)] += dp(i + 1, False, new_change, memo)
                return memo[(i, is_changed)]
            else:
                total = 0
                for j in range(digits[i]+1):
                    if j in invalid:
                        continue
                    new_change = is_changed
                    if j in change:
                        new_change = True
                    new_constrained = constrained and (j == digits[i])
                    total += dp(i+1, new_constrained, new_change, memo)
                return total
        return dp(0, True, False, {})