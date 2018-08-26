package TwoSum

import org.junit.jupiter.api.Test

class SolutionKTTest {

    @Test
    fun testTwoSum() {
        assert(SolutionKT().twoSum(intArrayOf(2, 5, 5, 11), 10).contentEquals(intArrayOf(1, 2)))
    }
}