class Solution {
public:
    vector<string> twoEditWords(vector<string>& queries, vector<string>& dictionary) {
        vector<string> ans;
        const int qz=queries.size(), sz=queries[0].size();
        for(int j=0; j<qz; j++){
            const string& q=queries[j];
            for(const string& d: dictionary){
                int diff=0;
                for(int i=0; i<sz; i++){
                    diff+=q[i]!=d[i];
                    if (diff>2) break;
                }
                if (diff<=2) {
                    ans.push_back(q); 
                    break;
                }  
            }
        }
        return ans;
    }
};