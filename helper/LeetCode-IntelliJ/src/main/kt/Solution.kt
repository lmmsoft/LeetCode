package kt

class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        for (i in nums.indices) {
            for (j in nums.indices) {
                if (i == j)
                    continue
                if (nums[i] + nums[j] == target)
                    return intArrayOf(i, j)
            }
        }

        return intArrayOf(0, 0)
    }
}