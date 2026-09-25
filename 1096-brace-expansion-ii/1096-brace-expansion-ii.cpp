class Solution {
public:
    vector<char> op;
    vector<vector<string>> st;

    void perf() {
        int x=st.size()-2, y = st.size()-1;
        if (op.back()=='+'){
            // Union
            st[x].reserve(st[x].size()+st[y].size());
            st[x].insert(st[x].end(), st[y].begin(), st[y].end());
        }
        else { // op.back()=='*'
            // Concatenation
            vector<string> nxt;
            nxt.reserve(st[x].size()*st[y].size());
            for (const auto& l : st[x]) {
                for (const auto& r : st[y]) 
                    nxt.push_back(l+r);
            }
            st[x]=move(nxt);
        }
        op.pop_back();
        st.pop_back();
    }
    vector<string> braceExpansionII(string& expr) {
        const int n=expr.size();
        op.reserve(n);

        char prv='@', cur;

        for (int i=0; i<n; i++, prv=cur) {
            cur = expr[i];
            switch (cur) {
            case ',': 
                while (!op.empty() && op.back() != '{') perf();
                op.push_back('+');
                break;
            case '{':
                if (prv=='}' || isalpha(prv)) op.push_back('*');
                op.push_back('{');
                break;
            case '}':
                while (!op.empty() && op.back()!='{') perf();
                op.pop_back(); // Remove matching '{'
                break;
            default:
                if (prv=='}') op.push_back('*');
                string s;
                for (; i<n && isalpha(expr[i]); i++) s+=expr[i];
                st.push_back({s});
                i--;
                cur=expr[i];
            }
        }

        while (!op.empty()) perf();

        auto ans=st.front();
        sort(ans.begin(), ans.end());
        ans.erase(unique(ans.begin(), ans.end()), ans.end());
        return ans;
    }
};

auto init = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 'c';
}();