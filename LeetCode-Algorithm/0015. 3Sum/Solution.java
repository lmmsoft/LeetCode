package ja;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;


class Solution {
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