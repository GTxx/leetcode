use std::collections::HashSet;

struct Solution;
impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut max_sub_str_len = 0;
        let (mut begin, mut end) = (0, 0);
        for (idx, c) in s.chars().enumerate() {
            if end > begin{
                // find in sub string, and change begin
                if let Some(begin1) = s.get(begin..end).unwrap().find(c) {
                    begin = begin1 + begin + 1;
                }
            }

            end = idx + 1;
            if  end - begin > max_sub_str_len {
                max_sub_str_len = end - begin;
            }
        }
        return max_sub_str_len as i32;
    }
}
#[cfg(test)]
mod tests {
    use crate::Solution;

    #[test]
    fn test_empty_string() {
        assert_eq!(Solution::length_of_longest_substring(String::from("")), 0);
    }

    #[test]
    fn test_1() {
        assert_eq!(Solution::length_of_longest_substring(String::from("abcabcbb")), 3);
    }

    #[test]
    fn test_2() {
        assert_eq!(Solution::length_of_longest_substring(String::from("bbbbb")), 1);
    }

    #[test]
    fn test_3() {
        assert_eq!(Solution::length_of_longest_substring(String::from("pwwkew")), 3);
    }

    #[test]
    fn test_4() {
        assert_eq!(Solution::length_of_longest_substring(String::from("tmmzixt")), 5);
    }
}
fn main() {
    println!("Hello, world!");
}
