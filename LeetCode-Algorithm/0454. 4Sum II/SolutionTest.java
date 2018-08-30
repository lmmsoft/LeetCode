package ja;

import org.junit.Assert;
import org.junit.Test;

public class SolutionTest {
    /*
        A = [ 1, 2]
        B = [-2,-1]
        C = [-1, 2]
        D = [ 0, 2]
     */

    @Test
    public void fourSumCount() {
        int[] A = {1, 2};
        int[] B = {-2, -1};
        int[] C = {-1, 2};
        int[] D = {0, 2};
        Assert.assertEquals(2, new Solution().fourSumCount(A, B, C, D));
    }
}