package ja;

import java.util.HashMap;

class Solution {
    public int fourSumCount(int[] A, int[] B, int[] C, int[] D) {
        HashMap<Integer, Integer> h1 = new HashMap<>();
        HashMap<Integer, Integer> h2 = new HashMap<>();
        getHash(A, B, h1);
        getHash(C, D, h2);
        int count = 0;
        for (int sum : h1.keySet()) {
            if (h2.get(-sum) != null) {
                count += h1.get(sum) * h2.get(-sum);
            }
        }
        return count;

    }

    private void getHash(int[] A, int[] B, HashMap<Integer, Integer> h1) {
        for (int i = 0; i < A.length; ++i) {
            for (int j = 0; j < B.length; ++j) {
                h1.merge(A[i] + B[j], 1, (a, b) -> a + b);
            }
        }
    }
}