import bisect


# 写法不好，用两个dict记录数据
class TimeMap1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.dv = {}

    def set(self, key: 'str', value: 'str', timestamp: 'int') -> 'None':
        if self.d.get(key):
            l = self.d.get(key)
            bisect.insort(l, timestamp)

            self.dv[key][timestamp] = value
        else:
            l = []
            bisect.insort(l, timestamp)
            self.d[key] = l

            self.dv[key] = {timestamp: value}

    def get(self, key: 'str', timestamp: 'int') -> 'str':
        if self.d.get(key):
            l = self.d.get(key)
            index = bisect.bisect_left(l, timestamp)
            if index < len(l) and l[index] == timestamp:
                print(self.dv[key][l[index]])
                return self.dv[key][l[index]]
            elif 0 < index < len(l) + 1:
                print(self.dv[key][l[index - 1]])
                return self.dv[key][l[index - 1]]
            else:
                print("")
                return ""
        else:
            print("")
            return ""


# 使用元组，一个dict里记录数据
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def set(self, key: 'str', value: 'str', timestamp: 'int') -> 'None':
        if self.d.get(key):
            bisect.insort(self.d[key], (timestamp, value))
        else:
            # 插入首个元素，不需要排序
            self.d[key] = [(timestamp, value)]

    def get(self, key: 'str', timestamp: 'int') -> 'str':
        res = ""
        if self.d.get(key):
            index = bisect.bisect(self.d[key], (timestamp,
                                                'z' * 101))  # value are lowers case length is [1,100],so zzzz...zzz is larger than any othter value
            if index == 0:
                res = ""
            else:
                res = self.d[key][index - 1][1]
        else:
            res = ""

        print(res)
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
if __name__ == '__main__':
    kv = TimeMap()
    kv.set("foo", "bar", 1);
    kv.get("foo", 1);  # 输出"bar"
    kv.get("foo", 3);  # 输出"bar"
    kv.set("foo", "bar2", 4);
    kv.get("foo", 4);  # 输出 "bar2"
    kv.get("foo", 5);  # 输出 "bar2"

    a = TimeMap()
    a.set("love", "high", 10)
    a.set("love", "low", 20)
    a.get("love", 5)
    a.get("love", 10)
    a.get("love", 15)
    a.get("love", 20)
    a.get("love", 25)
