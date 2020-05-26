struct Solution;
impl Solution {
    /// pick left bar and right bar, assume left bar is shorter then right bar
    /// if the second bar next to left bar is shorter then left bar, then water can
    /// be definitly filled in this bar.
    /// accumulate the water and change the second bar height to the left bar height.
    /// if the second bar height is taller then the left bar height, then it can hold no
    /// water, so set the left bar to the second bar
    pub fn trap(height: Vec<i32>) -> i32 {
        if height.is_empty() {
            return 0;
        }
        let mut height1 = height;
        let mut left: usize = 0;
        let mut right: usize = height1.len() - 1;
        let mut res = 0;
        while left < right {
           if height1.get(left)<= height1.get(right) {
              if left + 1 < right {
                  if height1[left+1] < height1[left] {
                      res += height1[left] - height1[left + 1];
                      height1[left + 1] = height1[left];
                  }
                  left = left + 1;
              } else {
                  break;
              }
           } else {
               if right -1 > left {
                   if height1[right] > height1[right-1] {
                       res += height1[right] - height1[right-1];
                       height1[right-1] = height1[right];
                   }
                   right -= 1;
               } else {
                   break;
               }
           }
        }
        res
    }
}

fn main() {
    let mut v = vec![0,1,0,2,1,0,1,3,2,1,2,1];
    assert_eq!(Solution::trap(v), 6);
    v = vec![0,1,0,2,1,0,1,3,2,1,2,1];
    println!("{}", Solution::trap(v));
    println!("{}", Solution::trap(vec![]));

}
