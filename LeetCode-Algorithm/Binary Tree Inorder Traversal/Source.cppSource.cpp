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
    vector<int> inorderTraversal(TreeNode *root){
        vector<int> v;
        v.clear();

        stack<pair<TreeNode*, bool> > s;
        while (!s.empty())
        {
            s.pop();
        }

        if (root == nullptr)
            return v;

        s.push(make_pair(root, false));
        while (!s.empty())
        {
            pair<TreeNode*, bool> p = s.top();
            s.pop();

            if (p.second)//second==true mean put into stack twice
                v.push_back(p.first->val);
            else{

                if (p.first->right != nullptr)
                    s.push(make_pair(p.first->right, false));

                s.push(make_pair(p.first, true));

                if (p.first->left != nullptr)
                    s.push(make_pair(p.first->left, false));
            }
        }
        return v;
    }
};

vector<int> v;
class Solution2 {
public:
    vector<int> inorderTraversal(TreeNode *root){
        v.clear();//without this line, judge will return WA, T_T
        f(root);
        return v;
    }
    void f(TreeNode *r)
    {
        if (r == NULL){
            return;
        }

        f(r->left);
        v.push_back(r->val);
        f(r->right);
    }
};

int main()
{
    Solution s;
    TreeNode t1 = TreeNode(1);
    TreeNode t2 = TreeNode(2);
    t1.left = &t2;

    vector<int> vv = s.inorderTraversal(&t1);
    for (vector<int>::iterator it = vv.begin(); it != vv.end(); ++it){
        cout << *it << " ";
    }
    cout << endl;
    system("pause");
}
