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
    pub fn remove_zero_sum_sublists(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        if let Some(mut node) = head {
            let mut tail = Self::remove_zero_sum_sublists(node.next.take());
            if node.val == 0 {
                return tail;
            }
            let mut sum = 0;
            let mut current_ref = tail.as_mut();
            while let Some(node1) = current_ref {
                sum += node1.val;
                if sum == -node.val {
                    return node1.next.take();
                }
                current_ref = node1.next.as_mut();
            }
            node.next = tail;
            Some(node)
        } else {
            None
        }
    }
}
#[cfg(test)]
mod tests {
    use crate::{ListNode, Solution};

    #[test]
    fn test() {
        assert_eq!(
            Solution::remove_zero_sum_sublists(ListNode::from(vec![1, 2, -3, 3, 1])),
            ListNode::from(vec![1, 2, 1])
        );
        assert_eq!(
            Solution::remove_zero_sum_sublists(ListNode::from(vec![1, 2, 3, -3, 4])),
            ListNode::from(vec![1, 2, 4])
        );
        assert_eq!(
            Solution::remove_zero_sum_sublists(ListNode::from(vec![1, 2, 3, -3, -2])),
            ListNode::from(vec![1])
        );
    }
}
fn main() {
    println!("Hello, world!");
}
