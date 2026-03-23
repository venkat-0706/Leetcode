class Solution
{
public:
    [[nodiscard]] constexpr int maxProductPath(
        const std::vector<std::vector<int>>& g) const noexcept
    {
        int64_t dp_lo[16], dp_hi[16];

        // for the first row the only
        // possible previous cell is 'left'
        for (int64_t p = 1; auto [x, v]: g[0] | views::enumerate) {
            dp_lo[x] = dp_hi[x] = p *= v;
        }

        // the rest
        for (auto& row: g | views::drop(1))
        {
            // for the first column the only
            // possible previous cell is 'up'
            dp_hi[0] *= row[0], dp_lo[0] *= row[0];

            for (auto[x, v]: row | views::enumerate | views::drop(1))
            {
                auto a = dp_lo[x - 1] * v;
                auto b = dp_lo[x] * v;
                auto c = dp_hi[x - 1] * v;
                auto d = dp_hi[x] * v;
                dp_lo[x] = min(min(a, b), min(c, d));
                dp_hi[x] = max(max(a, b), max(c, d));
            }
        }

        return max(dp_hi[g[0].size() - 1], -1L) % 1'000'000'007;
    }
};