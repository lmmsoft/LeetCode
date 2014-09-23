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

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *l1, *l2;
        if (head == NULL)
            return false;
        l1 = head;
        l2 = head;
        do
        {
            if (l2->next == NULL || l2->next->next == NULL){
                return false;
            }
            l2 = l2->next->next;
            l1 = l1->next;
        } while (l1 != l2);
        return true;
    }
};

int main()
{
    Solution s;
    ListNode l1 = ListNode(1);
    cout << s.hasCycle(&l1) << endl;

    ListNode l2 = ListNode(2);
    l1.next = &l2;
    cout << s.hasCycle(&l1) << endl;

    l2.next = &l1;
    cout << s.hasCycle(&l1) << endl;

    ListNode l3 = ListNode(3);
    ListNode l4 = ListNode(4);
    l2.next = &l3;
    l3.next = &l4;
    l4.next = &l2;
    cout << s.hasCycle(&l1) << endl;

    //point to self

    l1.next = &l1;
    cout << s.hasCycle(&l1) << endl;

    system("pause");
}