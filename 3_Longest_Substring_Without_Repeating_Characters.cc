    int lengthOfLongestSubstring(string s) {
        if(s.empty()) return 0;
        if(s.size()==1) return 1;
        map<char,int > m;
        int max_len = 0;
        int cur_len = 0;
        int loc = 0;
        for(int i = 0;i<s.size();++i){
            if(m.count(s[i])){
                loc = m[s[i]];
                if(loc>i-1-cur_len && loc<=i-1) {cur_len = i - loc;} 
                else {cur_len += 1;}
            }
            else{
                cur_len += 1;
            }
            m[s[i]] = i;
            if(cur_len > max_len) max_len = cur_len;
        }
        return max_len;
    }