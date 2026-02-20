class Solution {
public:
    string makeLargestSpecial(string s) {
        int i = 0;
        return dfs(s, i);
    }

private:
    string dfs(string& s, int& i) {
        string res;
        vector<string> toks;
        while (i < s.size() && res.empty()) {
            if (s[i++] == '1') toks.push_back(dfs(s, i));
            else res += "1";
        }
        bool prefix = res.size();
        sort(toks.begin(), toks.end());
        for (auto it = toks.rbegin(); it != toks.rend(); it++) res += *it;
        if (prefix) res += '0';
        return res;
    }
};