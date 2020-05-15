use std::cmp::max;

/// This problem is equivalent to get max of max turbulence size of all vec ends from
/// 1 to vec.len()
impl Solution {
    pub fn max_turbulence_size(a: Vec<i32>) -> i32 {
        let mut pre_num = a[0];
        let mut order: Option<bool> = None;
        let mut pre_turbulence_size = 1;
        let mut max_size = 1;
        for i in 1..a.len() {
            if let Some(is_bigger) = order {
                if is_bigger {
                    if a[i] < pre_num {
                        order = Some(false);
                        pre_turbulence_size += 1;
                    } else if a[i] > pre_num {
                        order = Some(true);
                        pre_turbulence_size = 2;
                    } else {
                        order = None;
                        pre_turbulence_size = 1;
                    }
                } else {
                    if a[i] > pre_num {
                        order = Some(true);
                        pre_turbulence_size += 1;
                    } else if a[i] < pre_num {
                        order = Some(false);
                        pre_turbulence_size = 2;
                    } else {
                        order = None;
                        pre_turbulence_size = 1;
                    }
                }
            } else {
                if a[i] == pre_num {
                    pre_turbulence_size = 1;
                } else {
                    order = Some(a[i] > pre_num);
                    pre_turbulence_size = 2;
                }
            }
            pre_num = a[i];
            max_size = max(max_size, pre_turbulence_size);
        }
        return max_size;
    }
}

fn main() {
    assert_eq!(
        Solution::max_turbulence_size(vec![9, 4, 2, 10, 7, 8, 8, 1, 9]),
        5
    );
    assert_eq!(Solution::max_turbulence_size(vec![4, 8, 12, 16]), 2);
    assert_eq!(Solution::max_turbulence_size(vec![100]), 1);
}
