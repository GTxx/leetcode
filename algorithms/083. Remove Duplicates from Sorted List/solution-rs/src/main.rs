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
        let mut result = ListNode::new(0);
        let mut current = &mut result;
        for i in v.iter() {
            let list_node = ListNode::new(*i);
            current = current.next.get_or_insert(Box::new(list_node));
        }
        return result.next;
    }
}
struct Solution;
impl Solution {
    pub fn delete_duplicates(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        head.map(|mut node| {
            let mut tail = node.next.take();
            let mut prev = &mut node;
            while let Some(mut current_node) = tail.take() {
                if current_node.val == prev.val {
                    tail = current_node.next.take();
                } else {
                    tail = current_node.next.take();
                    prev = prev.next.get_or_insert(current_node)
                }
            }
            return node;
        })
    }
}

#[cfg(test)]
mod tests {
    use crate::{ListNode, Solution};

    #[test]
    fn test() {
        assert_eq!(
            Solution::delete_duplicates(ListNode::from(vec![])),
            ListNode::from(vec![])
        );

        assert_eq!(
            Solution::delete_duplicates(ListNode::from(vec![1, 2])),
            ListNode::from(vec![1, 2])
        );

        assert_eq!(
            Solution::delete_duplicates(ListNode::from(vec![1, 1, 2])),
            ListNode::from(vec![1, 2])
        );
        assert_eq!(
            Solution::delete_duplicates(ListNode::from(vec![1, 1, 2, 2, 3])),
            ListNode::from(vec![1, 2, 3])
        );
    }
}
fn main() {
    println!("Hello, world!");
}
