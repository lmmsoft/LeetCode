# Link
- Description
    - https://leetcode.com/problems/rotate-array/
    - https://leetcode-cn.com/problems/rotate-array/
- Official Solution
    - https://leetcode.com/problems/rotate-array/solution/
    - No Chinese

# Solution
1. Brute Force
    - Everytime move 1 step, move k times
    - Time O(kN) Space O(1)
1. Using Extra Array
    - Move into new array
    - Space O(N)
1. Using Cyclic Replacements
    - Move nums[i] to nums[(i+k)%length]
    - Then move nums[(i+k)%length] to nums[(i+2k)%length]
    - Move length times in all
    - When length % k == 0, which means (i+j*k) % lenght == i, we start to move i+1
    - Time O(kN) Space O(1), but hard to implement
1. Using Reverse
    - reverse all nums
    - reverse nums[0,k)
    - reverse nums[k,length)
    - Time O(kN) Space O(1), easy to implement