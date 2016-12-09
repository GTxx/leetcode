package com.xx;
import java.util.Arrays;

public class Solution {
    public int removeElement(int[] nums, int val) {
        int high = nums.length-1;
        int low = 0;
        while (low <= high){
            if (nums[high] == val){
                high--;
            }
            else if (nums[low] == val){
                nums[low] = nums[high];
                low++;
                high--;
            }
            else {
                low++;
            }
        }
        return high + 1;
    }

    public static void main(String [] args){
        Solution s = new Solution();
        System.out.println(s.removeElement(new int[]{3,2,2,3}, 3));
    }
}