class Solution {
public:
    long long minimumTotalDistance(vector<int>& robot, vector<vector<int>>& factory) {
        // Sort robots and factories
        sort(robot.begin(), robot.end());
        sort(factory.begin(), factory.end());

        int m = robot.size();
        int n = factory.size();

        vector<vector<long long>> dp(m + 1, vector<long long>(n + 1, 0));

        // Base case: no factories left
        for (int i = 0; i < m; i++) {
            dp[i][n] = LLONG_MAX;
        }

        // Process factories from right to left
        for (int j = n - 1; j >= 0; j--) {
            long long prefix = 0;

            // deque of pair<index, value>
            deque<pair<int, long long>> dq;
            dq.push_back({m, 0});

            for (int i = m - 1; i >= 0; i--) {
                prefix += abs(robot[i] - factory[j][0]);

                // Remove out of capacity
                while (!dq.empty() && dq.front().first > i + factory[j][1]) {
                    dq.pop_front();
                }

                // Maintain monotonic deque
                long long val = dp[i][j + 1] - prefix;
                while (!dq.empty() && dq.back().second >= val) {
                    dq.pop_back();
                }

                dq.push_back({i, val});

                dp[i][j] = dq.front().second + prefix;
            }
        }

        return dp[0][0];
    }
};