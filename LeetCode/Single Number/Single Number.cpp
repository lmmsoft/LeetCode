#include <iostream>

using namespace std;

class Solution {
public:
    int singleNumber(int A[], int n) {
        int ans = 0;
        for (int i = 0; i < n; ++i)
        {
            ans ^= A[i];
        }
        return ans;
    }
};

int main()
{
    Solution s;
    cout << s.singleNumber(new int[]{1, 2, 1}, 3) << endl;
}