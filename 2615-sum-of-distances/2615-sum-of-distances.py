class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        mp = defaultdict(list)

        for i, v in enumerate(nums):
            mp[v].append(i)

        for pos in mp.values():
            total = sum(pos)
            left_sum = 0
            m = len(pos)

            for i in range(m):
                right_sum = total - left_sum - pos[i]

                left = pos[i] * i - left_sum
                right = right_sum - pos[i] * (m - i - 1)

                ans[pos[i]] = left + right

                left_sum += pos[i]

        return ans