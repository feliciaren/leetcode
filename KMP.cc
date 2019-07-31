#include<iostream>
#include<vector>
#include<string>

using namespace std;


vector<int> build_next(string s){
    int n = s.size(),i = 0,t = -1;
    vector<int> next(n,0);
    next[0] = -1;
    while(i<n-1){
        if(0>t||s[i]==s[t]){
            i++;
            t++;
            next[i] = (s[i] != s[t])? t:next[t];
        }else{
            t = next[t];
        }
    }
    return next;
}

int match(string s1,string s2){
    vector<int> next = build_next(s2);
    int i = 0,j = 0,m = s1.size(),n = s2.size();
    while(i<m && j<n){
        if(0>j||s1[i]==s2[j]){
            i++;
            j++;
        }
        else{
            j = next[j];
        }
    }
    return i-j;
}



int main(){
    string s1,s2;
    cin>>s1>>s2;
    cout<<match(s1,s2)<<endl;
    return 0;
}