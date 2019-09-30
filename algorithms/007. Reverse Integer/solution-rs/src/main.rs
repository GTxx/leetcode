struct Solution{}
impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let is_positive = x > 0;
        let mut abs_x = if x >0 {x as i64} else { -(x as i64)};
        let mut v: Vec<i64> = vec![];
        while abs_x != 0 {
            v.push(abs_x % 10);
            abs_x = abs_x / 10;
        }
        let mut result: i64 = 0;
        for i in v {
            result = result * 10 + i as i64;
        }
        if is_positive && result > (1i64 << 31) - 1{
            return 0;
        }
        if !is_positive && result >  1i64 << 31 {
            return 0;
        }
        if is_positive {result as i32} else {-result as i32}
    }
}

#[cfg(test)]
mod tests {

    use crate::Solution;
    #[test]
    fn test1() {
        assert_eq!(Solution::reverse(123), 321);
        assert_eq!(Solution::reverse(-123), -321);
        assert_eq!(Solution::reverse(10), 1);
    }

    #[test]
    fn test2() {
        assert_eq!(Solution::reverse(1534236469), 0);
    }

    #[test]
    fn test3() {
        assert_eq!(Solution::reverse(-1563847412), 0);
    }

    #[test]
    fn test4() {
        assert_eq!(Solution::reverse(-2147483648), 0);
    }

    #[test]
    fn test5() {
        assert_eq!(Solution::reverse(1463847412), 2147483641);
    }
}
fn main() {
    println!("Hello, world!");
}
