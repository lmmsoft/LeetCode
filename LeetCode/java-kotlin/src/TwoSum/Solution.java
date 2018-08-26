package TwoSum;

import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        return hashMap(nums, target);

        //return force(nums, target);
    }

    private int[] hashMap(int[] nums, int target) {
        HashMap<Integer, Integer> hashMap = new HashMap<>();// <number,index>
        for (int index = 0; index < nums.length; index++) {
            if (hashMap.containsKey(target - nums[index])) {
                int j = hashMap.get(target - nums[index]);
                return new int[]{j, index};
            } else {
                hashMap.put(nums[index], index);
            }
        }

        return new int[]{0, 0};
    }

    private int[] force(int[] nums, int target) {
        for (int i = 0; i < nums.length - 1; ++i) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }
        return new int[]{0, 0};
    }
}