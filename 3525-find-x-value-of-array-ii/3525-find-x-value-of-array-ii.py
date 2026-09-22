class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        nums = [x % k for x in nums]
        
        tree_prod = [0] * (4 * n)
        tree_remain = [[0] * k for _ in range(4 * n)]
        
        def merge(left_prod, left_remain, right_prod, right_remain):
            prod = (left_prod * right_prod) % k
            remain = list(left_remain)
            for i in range(k):
                remain[(i * left_prod) % k] += right_remain[i]
            return prod, remain

        def build(node, l, r):
            if l == r:
                val = nums[l]
                tree_prod[node] = val
                rem = [0] * k
                rem[val] = 1
                tree_remain[node] = rem
                return
            mid = (l + r) // 2
            build(2 * node, l, mid)
            build(2 * node + 1, mid + 1, r)
            p_l, rem_l = tree_prod[2 * node], tree_remain[2 * node]
            p_r, rem_r = tree_prod[2 * node + 1], tree_remain[2 * node + 1]
            tree_prod[node], tree_remain[node] = merge(p_l, rem_l, p_r, rem_r)

        def update(node, l, r, idx, val):
            if l == r:
                tree_prod[node] = val
                rem = [0] * k
                rem[val] = 1
                tree_remain[node] = rem
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(2 * node, l, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, r, idx, val)
            p_l, rem_l = tree_prod[2 * node], tree_remain[2 * node]
            p_r, rem_r = tree_prod[2 * node + 1], tree_remain[2 * node + 1]
            tree_prod[node], tree_remain[node] = merge(p_l, rem_l, p_r, rem_r)

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree_prod[node], tree_remain[node]
            mid = (l + r) // 2
            if qr <= mid:
                return query(2 * node, l, mid, ql, qr)
            elif ql > mid:
                return query(2 * node + 1, mid + 1, r, ql, qr)
            else:
                p_l, rem_l = query(2 * node, l, mid, ql, qr)
                p_r, rem_r = query(2 * node + 1, mid + 1, r, ql, qr)
                return merge(p_l, rem_l, p_r, rem_r)

        build(1, 0, n - 1)
        
        ans = []
        for index_i, value_i, start_i, xi in queries:
            v = value_i % k
            update(1, 0, n - 1, index_i, v)
            _, rem = query(1, 0, n - 1, start_i, n - 1)
            ans.append(rem[xi])
            
        return ans