package ja;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;


class Solution {
    //方法2(6ms): 简化条件，不需要和前第一个数比较，只有和前面第二个数比较
    // 如果不同就可以添加到尾部(最坏情况就是前面两个都相同嘛)
    // 如果相同就不能添加到尾部（因为数字是递增的，相同代表连续三个都一样）
    public int removeDuplicates(int[] nums) {
        if (nums.length <= 2) {
            return nums.length;
        }

        int j = 2;
        //去除重复的条件：数字重复且超过两个
        //保留的条件：数字不重复 或者 数字重复但是之前只有一个
        for (int i = 2; i < nums.length; ++i) {
            if (nums[i] != nums[j - 2]) {
                nums[j++] = nums[i];
            }
        }
        return j;
    }

    //方法1(10ms)：使用 "保留的条件"进行判断
    public int removeDuplicates2(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }

        int j = 0;
        //去除重复的条件：数字重复且超过两个
        //保留的条件：数字不重复 或者 数字重复但是之前只有一个
        for (int i = 1; i < nums.length; ++i) {
            if (nums[i] != nums[j]
                    || (nums[i] == nums[j] && (j < 1 || nums[i] != nums[j - 1]))) {
                nums[++j] = nums[i];
            }
        }
        return j + 1;
    }
}