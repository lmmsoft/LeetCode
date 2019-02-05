# link
- https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
- https://leetcode-cn.com/problems/vertical-order-traversal-of-a-binary-tree/
- https://leetcode.com/contest/weekly-contest-122/problems/vertical-order-traversal-of-a-binary-tree/
- https://leetcode-cn.com/contest/weekly-contest-122/problems/vertical-order-traversal-of-a-binary-tree/

# solution
- official solution
    - https://leetcode-cn.com/articles/vertical-order-traversal-of-a-binary-tree/
- 数据结构题
    - 用深搜找简单到每个节点的值 (x, y) = val
    - 随后是这些值的排序问题
        - 先根据x从小到大
        - x相等根据y从大到小
        - x y 都相等根据val的值从小到大
    - 利用python自带的 sort() 方法排序元组 x,y,val
        - 有个小技巧不难想到，递归深搜的时候令 y = y+1， 这样y也是从小到大，不需要自定义排序函数了
    - 输出
        - 根据排好序的 (x,y,val) 元组，输出目标数组即可
        - 小技巧， 因为 x值是外层数组顺序，y是内层数组顺序，可以用dict来存储
            - dict(key)->value, key是x, value是(y,val)
            - 这样可以直接用value来构造内部数组，外部数组 dict.keys()排序即可
        - 直接用元组输出的精妙代码
        ```python
        for i, e in enumerate(ans): # i下标 e元组(x,y,val)
            if i == 0 or e[0] != ans[i-1][0]: # i==0刚开始，后面是x不等于上一个x，换x时先储存
                ai.append([e[2]])  # ai尾部添加新list, val值e[2] 作为首个元素
            else:
                ai[-1].append(e[2]) # ai最后一个元素(实际是个数组)尾部添加val
        return ai
        ```
        