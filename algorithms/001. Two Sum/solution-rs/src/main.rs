use std::collections::HashMap;

struct Solution {}
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        for i in 0..nums.len() {
            for j in i+1..nums.len() {
                if nums[i] + nums[j] == target {
                    return vec![i as i32, j as i32]
                }
            }
        }
        vec![]
    }

    // O(n)
    pub fn two_sum1(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map: HashMap<i32, i32> = HashMap::with_capacity(nums.len());
        for (i, num) in nums.iter().enumerate() {
            let a = target - *num;
            if let Some(j) = map.get(&a) {
                return vec![*j, i as i32]
            } else {
                map.insert(*num, i as i32);
            }
        }
        vec![]
    }
}

#[cfg(test)]
mod tests {
    use crate::Solution;

    #[test]
    fn test1() {
        let v = vec![2,7,11,15];
        assert_eq!(Solution::two_sum(v, 9), vec![0, 1])
    }

    #[test]
    fn test2() {
        let v = vec![2,7,11,15];
        assert_eq!(Solution::two_sum1(v, 9), vec![0, 1])
    }
}

fn main() {
}
