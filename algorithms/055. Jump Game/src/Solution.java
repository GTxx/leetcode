class Solution {
  public boolean canJump(int[] nums) {
    Integer maxArrive = 0;
    Integer index = 0;
    for (int num: nums) {
        if (maxArrive < num + index) {
          maxArrive = num + index;
        }
        if (maxArrive >= nums.length-1) {
          return true;
        }
        if (maxArrive.equals(index)){
          return false;
        }
      index += 1;
    }
    return maxArrive >= nums.length-1;
  }

  static public void main(String[] args) {
    Solution solution = new Solution();
    assert solution.canJump(new int[]{});
    assert solution.canJump(new int[]{0});
    assert !solution.canJump(new int[]{0, 1});
    assert solution.canJump(new int[]{1, 0});
    assert solution.canJump(new int[]{2, 3, 1, 1, 4});
    assert !solution.canJump(new int[]{3, 2, 1, 0, 4});
  }
}
