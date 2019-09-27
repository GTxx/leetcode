use std::iter::FromIterator;

struct Solution;
impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let mut prefix = '_';
        let mut sum = 0;
        for x in s.chars() {
            let special_rule_value = Self::special_rule(&String::from_iter(vec![prefix, x]));
            if special_rule_value != 0 {
                sum -= Self::rule(prefix.to_string().as_str());
                sum += special_rule_value;
            } else {
                prefix = x;
                sum += Self::rule(x.to_string().as_str());
            }
        }
        return sum;
    }

    pub fn rule(s: &str) -> i32 {
        match s {
            "I" => 1,
            "V" => 5,
            "X" => 10,
            "L" => 50,
            "C" => 100,
            "D" => 500,
            "M" => 1000,
            _ => 0
        }
    }

    pub fn special_rule(s: &str) -> i32 {
        match s {
            "IV" => 4,
            "IX" => 9,
            "XL" => 40,
            "XC" => 90,
            "CD" => 400,
            "CM" => 900,
            _ => 0
        }
    }
}

#[cfg(test)]
mod tests {
    use crate::Solution;

    #[test]
    fn test1() {
        assert_eq!(Solution::roman_to_int(String::from("III")), 3);
        assert_eq!(Solution::roman_to_int(String::from("IV")), 4);
        assert_eq!(Solution::roman_to_int(String::from("IX")), 9);
        assert_eq!(Solution::roman_to_int(String::from("LVIII")), 58);
        assert_eq!(Solution::roman_to_int(String::from("MCMXCIV")), 1994);
    }
}
fn main() {
    println!("Hello, world!");
}
