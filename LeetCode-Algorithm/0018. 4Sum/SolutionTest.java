package ja;

import org.junit.Assert;
import org.junit.Test;

import java.util.Arrays;

public class SolutionTest {
    /*
        Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

        A solution set is:
        [
          [-1,  0, 0, 1],
          [-2, -1, 1, 2],
          [-2,  0, 0, 2]
        ]
     */

    @Test
    public void fourSumCount() {
        int[] A = {1, 0, -1, 0, -2, 2};
        Assert.assertEquals(3, new Solution().fourSum(A, 0).size());

        int[] B = {-3, -2, -1, 0, 0, 1, 2, 3};
        Assert.assertEquals(8, new Solution().fourSum(B, 0).size());
    }
}