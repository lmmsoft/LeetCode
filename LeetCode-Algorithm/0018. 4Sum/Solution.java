package ja;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Set<List<Integer>> set = new HashSet<>();

        Arrays.sort(nums);
        for (int a = 0; a < nums.length-3; ++a) {
            for (int b = a + 1; b < nums.length-2; ++b) {
                for (int c = b + 1; c < nums.length-1; ++c) {
                    for (int d = c + 1; d < nums.length; ++d) {
                        if (nums[a] + nums[b] + nums[c] + nums[d] == target) {
                            set.add(Arrays.asList(nums[a], nums[b], nums[c], nums[d]));
                            break;
                        }
                    }
                }
            }
        }

        return new ArrayList<List<Integer>>(set);
    }
}