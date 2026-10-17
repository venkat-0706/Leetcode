class Solution {

    int solve(int n){
        int sum=0;
        while(n!=0){
            sum+=n%10;
            n=n/10;
        }
        return sum;
    }

  void helper(vector<int>&nums,vector<pair<int,int>>&temp){
      for(int i=0;i<nums.size();i++){
          int sum=solve(nums[i]);
           temp.push_back({sum,nums[i]});
      }
  }
    
public:
  int minSwaps(vector<int>& nums) {
    vector<pair<int,int>>temp;
    helper(nums,temp);
    sort(temp.begin(), temp.end(),[](const pair<int,int> &a, const pair<int,int> &b) {
        if (a.first != b.first) 
            return a.first<b.first;  
        return a.second<b.second;     
    });

    vector<int>a;
    for (int i=0;i<temp.size();i++){
        a.push_back(temp[i].second);
    }
    int n=nums.size();
    unordered_map<int,int>mp2;
    for( int i=0;i<n;i++){
        mp2[a[i]]=i;
    }
    unordered_map<int,int>mp;
      for(int i=0;i<n;i++){
          mp[i]=mp2[nums[i]];
      }
    vector<bool>visited(n,false);
    int cnt=0;
    for (int i=0;i<n;i++){
        if(visited[i] || mp[i]==i) continue;
        int cycle_size=0;
        int j=i;
        while(!visited[j]){
            visited[j]=true;
            j=mp[j];
            cycle_size++;
        }
        if(cycle_size>1){
            cnt+=(cycle_size-1);
        }
    }
    return cnt;
}
};