class Solution {
    class Result {
        public int sum = 0;
        public int start = 0;
        public int end = 0;
    }
    private Result getMaxSum(int[] arr) {
        Result result = new Result();
        for (int i = 0; i < arr.length; i ++) {
            if (arr[i] >= 0 && result.end == i) {
                result.sum += arr[i];
                result.end = i+1;
            } else if (arr[i] >= 0 && result.end < i) {
                int preSum = result.sum;
                for (int k = result.end; k < i ; k ++) {
                    preSum += arr[k];
                }
                if (preSum >= result.sum) {
                    result.sum = preSum;
                    result.end = i+1;
                }
            }
        }
        return result;
    }

    public int kConcatenationMaxSum(int[] arr, int k) {

        return 1;
    }
}