package kt

import kt.Solution
import org.junit.Test

class SolutionTest {

    @Test
    fun twoSum() {
        assert(Solution().twoSum(intArrayOf(2, 5, 5, 11), 10).contentEquals(intArrayOf(1, 2)))
    }
}