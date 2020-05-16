import java.util.ArrayList;
import java.util.List;

class Solution {
    public int getMaxInRange(int[] A, int start, int end) {
        int max = A[start];
        for (int k = start + 1; k < end; k ++) {
            if (max < A[k]) {
                max = A[k];
            }
        }
        return max;
    }
    public int maxSumAfterPartitioning(int[] A, int K) {
        List<Integer> dp = new ArrayList<>();
        dp.add(0);
        for (int i = 0; i < A.length; i ++) {
            int max = dp.get(i) + A[i];
            for (int j = i - 1; j >= 0 && i - j < K ; j--) {
                int maxInRange = getMaxInRange(A, j, i + 1);
                int current = maxInRange * (i - j+1) + dp.get(j);
                if (current > max) {
                    max = current;
                }
            }
            dp.add(max);
        }
        return dp.get(A.length);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.maxSumAfterPartitioning(new int[]{1, 15, 7, 9, 2,5, 10}, 3) == 84;
    }
}