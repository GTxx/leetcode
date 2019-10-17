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

    fn from(v: Vec<i32>) -> Option<Box<ListNode>> {
        let mut head = Box::new(ListNode::new(0));
        let mut head_ref = &mut head;
        for i in v {
            head_ref.next = Some(Box::new(ListNode::new(i)));
            head_ref = head_ref.next.as_mut().unwrap();
        }
        return head.next;
    }
}

struct Solution;
impl Solution {
    pub fn delete_duplicates(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut new_head = Some(Box::new(ListNode::new(0)));
        let mut tail = new_head.as_mut();
        let mut current = head;
        let mut prev_val = None;
        while let Some(mut current_node) = current {
            let next_val = current_node.next.as_ref().map(|node| node.val);
            let current_val = Some(current_node.val);
            current = current_node.next.take();
            if Some(current_node.val) != prev_val && Some(current_node.val) != next_val {
                tail = tail.map(|node| node.next.get_or_insert(current_node));
            }
            prev_val = current_val;
        }
        return new_head.and_then(|node| node.next);
    }
}

#[cfg(test)]
mod tests {
    use crate::{ListNode, Solution};

    #[test]
    fn test() {
        assert_eq!(
            Solution::delete_duplicates(ListNode::from(vec![1, 1])),
            ListNode::from(vec![])
        );
        assert_eq!(
            Solution::delete_duplicates(ListNode::from(vec![1, 1, 2])),
            ListNode::from(vec![2])
        );
        assert_eq!(
            Solution::delete_duplicates(ListNode::from(vec![1])),
            ListNode::from(vec![1])
        );
        assert_eq!(
            Solution::delete_duplicates(ListNode::from(vec![])),
            ListNode::from(vec![])
        );
        assert_eq!(
            Solution::delete_duplicates(ListNode::from(vec![1, 1, 1, 2, 3])),
            ListNode::from(vec![2, 3])
        );
    }
}
fn main() {
    println!("Hello, world!");
}
