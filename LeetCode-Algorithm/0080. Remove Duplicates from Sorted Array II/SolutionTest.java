package ja;

import org.junit.Assert;
import org.junit.Test;

import java.util.Arrays;

public class SolutionTest {

    @Test
    public void test() {

        {
            //sample 1
            int[] A = {1,1,1,2,2,3};
            Assert.assertEquals(5, new Solution().removeDuplicates(A));
            Assert.assertEquals(1, A[0]);
            Assert.assertEquals(1, A[1]);
            Assert.assertEquals(2, A[2]);
            Assert.assertEquals(2, A[3]);
            Assert.assertEquals(3, A[4]);
        }

        {
            //sample 2
            int[] A = {0,0,1,1,1,1,2,3,3};
            Assert.assertEquals(7, new Solution().removeDuplicates(A));
            Assert.assertEquals(0, A[0]);
            Assert.assertEquals(0, A[1]);
            Assert.assertEquals(1, A[2]);
            Assert.assertEquals(1, A[3]);
            Assert.assertEquals(2, A[4]);
            Assert.assertEquals(3, A[5]);
            Assert.assertEquals(3, A[6]);
        }

        {
            // test no change
            int[] A = {0, 1};
            Assert.assertEquals(2, new Solution().removeDuplicates(A));
            Assert.assertEquals(0, A[0]);
            Assert.assertEquals(1, A[1]);
        }

        {
            // test 0 num
            int[] A = {};
            Assert.assertEquals(0, new Solution().removeDuplicates(A));
        }
    }
}