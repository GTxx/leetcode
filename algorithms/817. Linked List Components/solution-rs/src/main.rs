use std::collections::HashSet;

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }

    // init list from vector
    fn from(v: Vec<i32>) -> Option<Box<ListNode>> {
        let mut head = Box::new(Self::new(0));
        let mut head_ref = &mut head;
        for i in v {
            head_ref = head_ref.next.get_or_insert(Box::new(ListNode::new(i)));
        }
        head.next
    }
}
struct Solution;
impl Solution {
    pub fn num_components(head: Option<Box<ListNode>>, g: Vec<i32>) -> i32 {
        let set: HashSet<i32> = g.into_iter().collect();
        let mut result = 0;
        let mut prev_is_in_g = false;
        let mut current = head.as_ref();
        while let Some(node) = current {
            if set.contains(&node.val) {
                prev_is_in_g = true
            } else {
                if prev_is_in_g {
                    result += 1;
                }
                prev_is_in_g = false
            }
            current = node.next.as_ref()
        }
        if prev_is_in_g {
            result += 1;
        }
        result
    }
}

#[cfg(test)]
mod tests {
    use crate::{ListNode, Solution};

    #[test]
    fn test() {
        assert_eq!(
            Solution::num_components(ListNode::from(vec![0, 1, 2, 3]), vec![0, 1, 3]),
            2
        );

        assert_eq!(
            Solution::num_components(ListNode::from(vec![0, 1, 2, 3, 4]), vec![0, 3, 1, 4]),
            2
        );
    }
}
fn main() {
    println!("Hello, world!");
}
