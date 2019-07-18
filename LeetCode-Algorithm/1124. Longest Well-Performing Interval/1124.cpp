class Solution {
public:
    int longestWPI(vector<int>& hours) {
        int cur_max = 0;
        int l = hours.size();
        for(int i=0;i<l;++i){
            int t=0;
            int r=0;
            if(l-i+1 < cur_max){
                break;
            }

            for(int j=i;j<l;++j){
                if(hours[j]>8){
                    t++;
                }else{
                    r++;
                }
                if(t>r){
                    int cur_len = j-i+1;
                    if(cur_len>cur_max){
                        cur_max=cur_len;
                    }
                }
            }
        }

        return cur_max;
    }
};