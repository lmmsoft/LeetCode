# link
- https://leetcode.com/problems/time-based-key-value-store/
- https://leetcode-cn.com/problems/time-based-key-value-store/
- https://leetcode.com/contest/weekly-contest-121/problems/time-based-key-value-store/
- official solution
    - https://leetcode.com/articles/time-based-key-value-store/
    - https://leetcode-cn.com/articles/time-based-key-value-store/

# solution
- 外层map, 里层数据结构，要求能实现upper_bound(key)操作，即找到不大于key的最大值
    - C++里用map TreeMap都可以
    - python里不知道怎么实现，于是花了不少时间调研了一下
        - 找到bisect，可以把list插入排序，二分查找
    - 赛后看了大家的结果，python主要用bisect或者手写二分
    - 我用了两个dict记录数据，其实可以改用一个dict里的元组，更方便
        - 注意元组的默认排序，先按first再按second排序
        - 查找的时候second也会一起查，所以用右查询，first为timestamp,second为zz..zz
    - 还有一点需要注意
        - 题目描述里明确说明 "所有 TimeMap.set 操作中的时间戳 timestamps 都是严格递增的。"
        - 这个可以保证插入数据时直接append，不需要排序
        - 而我没仔细看到这点，插入数据时考虑多了，先排序


# 其他实现
    - C++：unordered_map +  lower_bound
```c
class TimeMap {
    unordered_map<string,map<int,string>> mm;
public:
    /** Initialize your data structure here. */
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        if(mm.find(key)==mm.end()){
            mm[key]=map<int,string>();
        }
        mm[key][-timestamp]=value;
    }
    
    string get(string key, int timestamp) {
        if(mm.find(key)==mm.end()) return "";
        auto it=mm[key].lower_bound(-timestamp);
        if(it==mm[key].end()) return "";
        return it->second;
    }
};
```
    - C++: map + upper_bound
```c++
class TimeMap {
public:
    map<string, map<int, string>> M;
    /** Initialize your data structure here. */
    TimeMap() {
        M.clear();
    }
    
    void set(string key, string value, int timestamp) {
        M[key][timestamp]=value;
    }
    
    string get(string key, int timestamp) {
        auto it=M[key].upper_bound(timestamp);
        if (it==M[key].begin()) return "";
        it--;
        return it->second;
    }
};
```