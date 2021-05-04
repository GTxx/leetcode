use std::{cmp};

struct Solution;
struct Store {
    cache: Vec<Vec<i32>>
}

impl Store {
    pub fn new(n: i32) -> Self {
        Store {
            cache: vec![vec![0; n as usize]; n as usize]
        }
    }

    pub fn get_value(&self, from: i32, to: i32) -> i32 {
        if from >= to {
            return 0;
        } else if from + 1 == to {
            return from;
        } else {
            self.cache[(from-1) as usize][(to-1) as usize]
        }
    }

    pub fn set_value(&mut self, from: i32, to: i32, value: i32) {
        self.cache[(from-1) as usize][(to-1) as usize] = value;
    }
}
impl Solution {
    pub fn get_money_amount(n: i32) -> i32 {
        let mut cache_store = Store::new(n);
        for diff in 2..n {
            for j in 1..=n - diff {
                let (from, to) = (j, j + diff);
                let mut max_vec: Vec<i32> = vec![];
                for mid in from..=to {
                    let (left_from, left_to) = (from, mid - 1);
                    let (right_from, right_to) = (mid + 1, to);
                    max_vec.push(
                        cmp::max(mid + cache_store.get_value(left_from, left_to), mid
                            + cache_store.get_value(right_from, right_to))
                    );
                }
                let min_of_max = max_vec.iter().min().unwrap();
                cache_store.set_value(from, to, min_of_max.to_owned());
            }
        }
        cache_store.get_value(1, n)
    }
}

pub fn main() {
    assert_eq!(Solution::get_money_amount(4), 4);
    assert_eq!(Solution::get_money_amount(5), 6);
    assert_eq!(Solution::get_money_amount(10), 16);
    assert_eq!(Solution::get_money_amount(20), 49);
}
