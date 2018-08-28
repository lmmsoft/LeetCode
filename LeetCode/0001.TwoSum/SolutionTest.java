package ja;

import org.junit.Assert;
import org.junit.Test;

public class SolutionTest {

    @Test
    public void twoSum() {
        Assert.assertArrayEquals(new int[]{0, 1}, new Solution().twoSum(new int[]{2, 7, 11, 15}, 9));
    }
}