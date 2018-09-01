# 15 3Sum

```
类型：双指针
Time Complexity O(n^2)
Space Complexity O(1)
```

- 大概思路是外围写一个for循环，用于遍历数组的第一个数i的位置
    - 然后设left为i后一个数，right为最后一个数
    - 如果sum(num[i],num[left],num[right])==0，说明(i,left,right)是一组解
    - 如果sum<0，说明和小了，left右移一位，让总和变大
    - 如果sum>0，说明和大了，right左移一位，让总和变小
- 直到left>=right循环结束


- 此外还要注意去重，我这里取巧，把结果放hashset里，让set帮忙去重，这样时间复杂度是一样的，但是实际花的时间比代码里去重要慢不少49ms vs 293ms，题目里应该是有极端数据
- 参考代码:
``` java
    Set<List<Integer>> resultSet = new HashSet<>();
    int[] nums;

    public List<List<Integer>> threeSum(int[] nums) {
        this.nums = nums;
        if (nums.length < 3) {
            return new ArrayList<>(resultSet);
        }

        Arrays.sort(nums);

        for (int i = 0; i < nums.length - 2; ++i) {
            int left = i + 1;
            int right = nums.length - 1;

            while (left < right) {
                int sum = getSum(i, left, right);
                if (sum == 0) {
                    addResult(i, left, right);
                    left++;
                    right--;
                } else if (sum < 0) {
                    left++;
                } else if (sum > 0) {
                    right--;
                }
            }
        }

        return new ArrayList<>(resultSet);
    }

    int getSum(int i, int j, int k) {
        return nums[i] + nums[j] + nums[k];
    }

    void addResult(int i, int j, int k) {
        resultSet.add(Arrays.asList(nums[i], nums[j], nums[k]));
    }
}
```