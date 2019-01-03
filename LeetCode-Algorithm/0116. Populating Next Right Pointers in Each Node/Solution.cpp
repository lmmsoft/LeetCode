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


struct TreeLinkNode {
    int val;
    TreeLinkNode *left, *right, *next;
    TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
};

class Solution {
public:
    void connect(TreeLinkNode *root) {
        if (root != nullptr)
            f(root);
    }

    void f(TreeLinkNode *r)
    {
        if (r->left != nullptr){
            r->left->next = r->right;
            f(r->left);
        }

        if (r->right != nullptr){
            if (r->next == nullptr)
                r->right->next = nullptr;
            else
                r->right->next = r->next->left;
            f(r->right);
        }
    }
};

int main()
{
    Solution s;
    cout << endl;
    system("pause");
}
