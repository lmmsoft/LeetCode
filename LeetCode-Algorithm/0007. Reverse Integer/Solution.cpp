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
    int reverse(int x) {
        int r = 0;
        while (x)
        {
            r = r * 10 + x % 10;
            x = x / 10;
        }
        return r;
    }
};

int main()
{
    Solution s;
    cout << endl;
}