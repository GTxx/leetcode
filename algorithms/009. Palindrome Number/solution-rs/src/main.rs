struct Solution;

impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 { return false; }
        let mut v = vec![];
        let mut y = x;
        while y != 0 {
            v.push(y % 10);
            y = y / 10;
        }
        let mut start = 0;
        println!("v.len {}", v.len());
        while start + 1 + start <= v.len() {
            if v.get(start).unwrap() == v.get(v.len() - 1 - start).unwrap() {
                start += 1;
            } else {
                return false;
            }
        }
        true
    }
}

#[cfg(test)]
mod tests {
    use crate::Solution;

    #[test]
    fn test() {
        assert!(Solution::is_palindrome(121));
        assert!(!Solution::is_palindrome(-121));
        assert!(!Solution::is_palindrome(21));
        assert!(!Solution::is_palindrome(0));
    }
}

fn main() {
    println!("Hello, world!");
}
