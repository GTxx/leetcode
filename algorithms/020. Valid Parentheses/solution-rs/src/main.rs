struct Solution;
impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack:Vec<char> = vec![];
        for c in s.chars() {
            match c {
                '(' | '[' | '{' => stack.push(c),
                ')' | ']' | '}' => {
                    let poped = stack.pop();
                    if let Some(p) = poped {
                        if (p == '(' && c != ')') || (p == '[' && c != ']') || (p == '{' && c != '}') {
                            return false;
                        }
                    } else {
                        return false;
                    }
                }
                _ => panic!("can't handle")
            }
        }
        return stack.is_empty();

    }
}

#[cfg(test)]
mod tests {
    use crate::Solution;

    #[test]
    fn test1() {
        assert!(Solution::is_valid(String::from("()")));
        assert!(Solution::is_valid(String::from("()[]{}")));
        assert_eq!(Solution::is_valid(String::from("(]")), false);
        assert_eq!(Solution::is_valid(String::from("([)]")), false);
        assert!(Solution::is_valid(String::from("{[]}")));

    }
}
fn main() {
    println!("Hello, world!");
}
