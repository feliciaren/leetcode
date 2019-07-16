#include<iostream>
#include<string>
#include<stack>
using namespace std;
string decodeString(string s) {
    stack<pair<int,int>> st;
    string res;
    for(int i = 0;i<s.size();i++){
        // cout<<i<<endl;
        if(s[i]>='0' and s[i]<='9'){
            int tmp = s[i] - '0';
            while(i+1<s.size() and s[i+1]>='0' and s[i+1]<='9'){
                tmp = tmp * 10;
                tmp += s[++i]-'0';
            }
            // cout<<tmp;
            st.push(make_pair(tmp,res.size()));
        }
        else if(s[i]==']' and !st.empty()){
            auto &t = st.top();st.pop();
            int size = res.size();
            // cout<<size<<endl;
            if(t.first){
                while(t.first){
                    res += res.substr(t.second,size-t.second);
                    t.first--;
                }
            }
            else{
                res.erase(t.second,size);
            }
        }
        else if(s[i] != '[') res += s[i];
    }
    return res;
}
int main(){
    cout<<"Decode String: "<<endl;
    string s;
    cin>>s;
    cout<<s<<endl;
    cout<<"Decode Result: "<<endl;
    cout<<decodeString(s);
    return 0;
}