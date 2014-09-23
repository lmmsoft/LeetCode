#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int> &p) {
        int L = p.size();
        if (L < 2)
            return 0;
        int currentMin = p[0];
        int S = 0;
        bool up = true;
        for (int i = 1; i < L; ++i){
            if (p[i] >= p[i - 1]){
                up = true;
            }
            else{
                if (up){
                    S += p[i - 1] - currentMin;
                    //currentMin = p[i];
                }
                currentMin = p[i];
                up = false;
            }
        }
        return S + p[L - 1] - currentMin;
    }
};

int main()
{
    Solution s;

    int ary[] = { 2, 1, 3 };//2
    vector<int> v(ary, ary + 3);
    cout << s.maxProfit(v) << endl;

    int ary2[] = { 2, 4, 6, 3, 2, 5, 7 };//9
    vector<int> v2(ary2, ary2 + 7);
    cout << s.maxProfit(v2) << endl;
}
