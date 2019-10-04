struct Solution;
impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut result =0;
        let mut low: i32 = 0;
        let mut high :i32 = nums.len() as i32 - 1;
        while low <= high {
           if nums[high as usize] == val {
                high = high - 1;
               result += 1;
           } else if nums[low as usize] == val {
               nums[low as usize] = nums[high as usize];
               high = high - 1;
               low = low + 1;
               result += 1;
           } else {
               low = low + 1;
           }
        }

        return nums.len() as i32 - result ;
    }
}

#[cfg(test)]
mod tests {
    use crate::Solution;
    use std::collections::HashSet;
    use std::iter::FromIterator;

    fn should_equal(x: Vec<i32>, y: Vec<i32>) {
        let x1:HashSet<i32> = HashSet::from_iter(x);
        let y1:HashSet<i32> = HashSet::from_iter(y);
        assert_eq!(x1, y1);
    }
    #[test]
    fn test1() {
        let mut v = vec![1, 2, 3, 4];
        assert_eq!(Solution::remove_element(&mut v, 2), 3);
        should_equal(v, vec![1,3, 4] );

        let mut v = vec![];
        assert_eq!(Solution::remove_element(&mut v, 2), 0);
        should_equal(v, vec![] );

        let mut v = vec![ 0,1,2,2,3,0,4,2];
        assert_eq!(Solution::remove_element(&mut v, 2), 5);
        println!("remain v: {:?}", v);


    }
}

fn main() {
    println!("Hello, world!");
}
