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

        Map<Integer, Integer> mapValue = new HashMap<>();
        for (int num : nums) {
            mapValue.put(num, mapValue.getOrDefault(num, 0) + 1);
        }

        for (int a = 0; a < nums.length; ++a) {
            for (int b = a + 1; b < nums.length; ++b) {
                for (int c = b + 1; c < nums.length; ++c) {

                    int expect = target - nums[a] - nums[b] - nums[c];
                    Integer valueCount = mapValue.get(expect);
                    if (valueCount == null) {
                        continue;
                    } else if (valueCount == 1) {
                        if (expect != nums[a] && expect != nums[b] && expect != nums[c]) {
                            List<Integer> list =Arrays.asList(nums[a], nums[b], nums[c], expect);
                            list.sort((x,y)->(x-y));

                            set.add(list);
                        }

                    } else {
                        List<Integer> list =Arrays.asList(nums[a], nums[b], nums[c], expect);
                        list.sort((x,y)->(x-y));

                        set.add(list);
                    }

//                    for (int d = c + 1; d < nums.length; ++d) {
//                        if (nums[a] + nums[b] + nums[c] + nums[d] == target) {
//                            set.add(Arrays.asList(nums[a], nums[b], nums[c], nums[d]));
//                            break;
//                        }
//                    }
                }
            }
        }

        return new ArrayList<List<Integer>>(set);
    }

    public List<List<Integer>> fourSumForce(int[] nums, int target) {
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