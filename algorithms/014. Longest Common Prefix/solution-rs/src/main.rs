
struct Solution;

impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        let mut prefix: String = String::new();
        let mut idx :usize= 0;
        'outer: loop {
            let mut common: Option<char> = None;
            for str in strs.iter() {
                if let Some(a) = str.chars().nth(idx) {
                    if let Some(c) = common {
                        if c != a {
                            break 'outer;
                        }
                    } else {
                        common = Some(a);
                    }
                } else {
                    break 'outer;
                }
            }
            if let Some(c) = common {
                prefix.push(c);
                idx = idx + 1;
            } else {
                break;
            }
        }
        return prefix;
    }
}

#[cfg(test)]
mod tests {
    use crate::Solution;

    #[test]
    fn test1() {
        assert_eq!(Solution::longest_common_prefix(vec![String::from("flower"), String::from("flow"), String::from("flight")]), "fl");
    }

    #[test]
    fn test2() {
        assert_eq!(Solution::longest_common_prefix(vec![]), "");
    }
}
fn main() {
    println!("Hello, world!");
}
