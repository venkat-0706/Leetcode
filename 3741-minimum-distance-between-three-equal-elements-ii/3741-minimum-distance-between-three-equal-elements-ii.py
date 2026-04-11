from collections import defaultdict

class Solution:
    def minimumDistance(self, nums):
        mp = defaultdict(list)

        for i, num in enumerate(nums):
            mp[num].append(i)

        mini = float('inf')

        for temp in mp.values():
            m = len(temp)

            if m >= 3:
                for i in range(m - 2):
                    a = temp[i]
                    b = temp[i + 1]
                    c = temp[i + 2]

                    diff = 2 * (max(a, b, c) - min(a, b, c))
                    mini = min(mini, diff)

        return -1 if mini == float('inf') else mini