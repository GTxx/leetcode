import java.util.ArrayList;
import java.util.List;

class Solution {
  public int numSquares(int n) {
    List<Integer> dp = new ArrayList<>();
    dp.add(0);
    for(int i = 1; i < n+1; i++) {
      int min_num = i; // obvious solution is to sum 1 with i times
      for (int j = 2; j*j <= i; j ++) {
        if (dp.get(i-j*j) + 1 < min_num) {
          min_num = dp.get(i-j*j) + 1;
        }
      }
      dp.add(min_num);
    }
    return dp.get(n);
  }

  static public void main(String[] args) {
    Solution solution = new Solution();
    assert solution.numSquares(12) == 3;
    assert solution.numSquares(13) == 2;
  }
}