from typing import Dict


class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.d: Dict[Dict[int, int]] = {}  # num :  (snap_id, num) , default 0:0

    def set(self, index: int, val: int) -> None:
        if index in self.d:
            self.d[index][self.snap_id] = val
        else:
            self.d[index] = {0: 0}
            self.d[index][self.snap_id] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        if index in self.d:
            if snap_id in self.d[index]:
                return self.d[index][snap_id]
            else:
                # 找到前一个
                ii = 0
                for i in self.d[index].keys():
                    if i >= snap_id:
                        break
                    ii = i
                return self.d[index][ii]

        else:
            return 0

    # Your SnapshotArray object will be instantiated and called as such:
    # obj = SnapshotArray(length)
    # obj.set(index,val)
    # param_2 = obj.snap()
    # param_3 = obj.get(index,snap_id)


if __name__ == '__main__':
    # Case1
    s = SnapshotArray(3)
    s.set(0, 5)
    assert s.snap() == 0
    s.set(0, 6)
    assert s.get(0, 0) == 5

    # Case2
    s = None
    l1 = ["SnapshotArray", "set", "snap", "set", "snap", "set", "snap", "set", "get", "get", "snap"]
    l2 = [[4], [1, 5], [], [0, 16], [], [2, 15], [], [2, 5], [1, 0], [0, 2], []]
    null = None
    l3 = [null, null, 0, null, 1, null, 2, null, 5, 16, 3]
    for i in range(0, len(l1)):
        print(i)
        if l1[i] == "SnapshotArray":
            s = SnapshotArray(l2[i][0])
        elif l1[i] == "set":
            s.set(l2[i][0], l2[i][1])
        elif l1[i] == "snap":
            assert s.snap() == l3[i]
        elif l1[i] == 'get':
            assert s.get(l2[i][0], l2[i][1]) == l3[i]

    # Case3 without assert
    s = None
    l1 = ["SnapshotArray", "snap", "get", "get", "set", "get", "set", "get", "set"]
    l2 = [[2], [], [1, 0], [0, 0], [1, 8], [1, 0], [0, 20], [0, 0], [0, 7]]
    for i in range(0, len(l1)):
        print(i)
        if l1[i] == "SnapshotArray":
            s = SnapshotArray(l2[i][0])
        elif l1[i] == "set":
            s.set(l2[i][0], l2[i][1])
        elif l1[i] == "snap":
            s.snap()
        elif l1[i] == 'get':
            s.get(l2[i][0], l2[i][1])
