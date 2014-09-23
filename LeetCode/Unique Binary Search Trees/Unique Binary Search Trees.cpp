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

/*

A(x)= B(0,x-1)+B(1,x-2)+...+B(x-2,1)+B(x-1,0)
B(a,b)=A(a)*A(b)

A(0)=1
A(1)=1
A(2)=2
A(3)=B(1,1)+2*B(2,0)=A(1)*A(1)+2*A(2)*A(0) =1+2*2=5
A(4)=(B(0,3)+B(1,2))*2=2*(A(3)+A(2))=14
A(5)=B(2,2)+2*(B(0,4)+B(1,3))

*/

int A[1000];
class Solution {
public:
    int numTrees(int n) {
        memset(A, 0, sizeof(A));
        A[0] = 1;
        A[1] = 1;
        A[2] = 2;
        if (n < 3)
            return A[n];
        int sum = 0;
        for (int i = 3; i <= n; ++i)
        {
            sum = 0;
            for (int j = 0; j < i ; ++j)
            {
                sum += A[j] * A[i - j - 1];
            }
            A[i] = sum;
        }
        return A[n];
    }
};

int main()
{
    Solution s;

    cout << (s.numTrees(3)) << endl;
    cout << (s.numTrees(4)) << endl;
    system("pause");
}