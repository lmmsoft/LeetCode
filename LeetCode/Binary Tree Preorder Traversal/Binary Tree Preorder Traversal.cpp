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


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<int> preorderTraversal(TreeNode *root){
        vector<int> v;
        v.clear();

        stack<TreeNode*> s;
        while (!s.empty())
        {
            s.pop();
        }

        s.push(root);
        while (!s.empty())
        {
            TreeNode* t = s.top();
            s.pop();
            if (t != NULL){
                v.push_back(t->val);

                s.push(t->right);
                s.push(t->left);
            }
        }
        return v;
    }
};

vector<int> v;
class Solution2 {
public:
    vector<int> preorderTraversal(TreeNode *root){
        v.clear();//without this line, judge will return WA, T_T
        f(root);
        return v;
    }
    void f(TreeNode *r)
    {
        if (r == NULL){
            return;
        }
        v.push_back(r->val);
        f(r->left);
        f(r->right);
    }
};

int main()
{
    Solution s;
    TreeNode t = TreeNode(5);
    vector<int> vv = s.preorderTraversal(&t);
    for (vector<int>::iterator it = vv.begin(); it != vv.end(); ++it){
        cout << *it << " ";
    }
    cout << endl;
    system("pause");
}
