#include<vector>
#include<queue>
#include<iostream>
using namespace std;
int findKthLargest(vector<int>& nums,int k){
    priority_queue<int,vector<int>,greater<int>> q;
    for(int i = 0;i<k;i++){
        q.push(nums[i]);
    }
    for(int i = k;i<nums.size();i++){
        if(nums[i]>q.top()){
            q.pop();
            q.push(nums[i]);
        }
    }
    return q.top();
}
int main(){
    cout<<"Array Length: "<<endl;
    int n;
    cin>>n;
    vector<int> nums(n);
    cout<<"Array: "<<endl;
    for(int i = 0;i<n;i++){
        cin>>nums[i];
    }
    cout<<"K: "<<endl;
    int k;
    cin>>k;
    cout<<"Result: "<<endl;
    cout<<findKthLargest(nums,k);
    return 0;
}