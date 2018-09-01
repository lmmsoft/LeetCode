package ja;

import org.junit.Assert;
import org.junit.Test;

import java.util.Arrays;

public class SolutionTest {
    /*
        Given array nums = [-1, 0, 1, 2, -1, -4],

        A solution set is:
        [
          [-1, 0, 1],
          [-1, -1, 2]
        ]
     */

    @Test
    public void threeSumTest() {
        int[] A = {-1, 0, 1, 2, -1, -4};
        Assert.assertEquals(2, new Solution().threeSum(A).size());

        int[] B = {0, 0};
        Assert.assertEquals(0, new Solution().threeSum(B).size());

        int[] C = {-2, 0, 1, 1, 2};
        Assert.assertEquals(2, new Solution().threeSum(C).size());
    }
}