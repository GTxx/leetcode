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
        let mut l = Box::new(ListNode::new(0));
        let mut current = &mut l;
        for i in v {
            current.next = Some(Box::new(ListNode::new(i)));
            current = current.next.as_mut().unwrap();
        }
        return l.next;
    }
}
struct Solution;
impl Solution {
    pub fn is_palindrome(head: Option<Box<ListNode>>) -> bool {
        let mut mut_head = head;
        let length = Self::get_length(mut_head.as_ref());

        let middle = if length % 2 == 0 {
            length / 2
        } else {
            (length - 1) / 2
        };
        let (mut first, mut second) = Self::split_from(mut_head, middle);
        if length % 2 == 1 {
            second = second.and_then(|mut node| node.next.take());
        }
        first = Self::reverse(first);
        println!("{:?} {:?}", first, second);
        first == second
    }

    pub fn split_from(
        head: Option<Box<ListNode>>,
        n: i32,
    ) -> (Option<Box<ListNode>>, Option<Box<ListNode>>) {
        if n == 0 {
            return (None, head);
        }
        let mut i = 0;
        let mut mut_head = head;
        let mut current = mut_head.as_mut();
        while i < n - 1 {
            i += 1;
            if let Some(node) = current {
                current = node.next.as_mut();
            }
        }
        let res = current.and_then(|node| node.next.take());
        return (mut_head, res);
    }

    pub fn get_length(mut head: Option<&Box<ListNode>>) -> i32 {
        let mut i = 0;
        while let Some(p) = head {
            head = p.next.as_ref();
            i += 1;
        }
        return i;
    }

    pub fn reverse(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut tail = None;
        let mut mut_head = head;
        while let Some(mut node) = mut_head.take() {
            let next = node.next.take();
            node.next = tail;
            tail = Some(node);
            mut_head = next;
        }
        return tail;
    }
}

#[cfg(test)]
mod tests {
    use crate::{ListNode, Solution};

    #[test]
    fn test() {
        assert_eq!(
            Solution::split_from(ListNode::from(vec![1, 2]), 1),
            (ListNode::from(vec![1]), ListNode::from(vec![2]))
        );
        assert_eq!(
            Solution::split_from(ListNode::from(vec![1]), 1),
            (ListNode::from(vec![1]), ListNode::from(vec![]))
        );
    }
    #[test]
    fn test1() {
        assert_eq!(
            Solution::reverse(ListNode::from(vec![1, 2, 3])),
            ListNode::from(vec![3, 2, 1])
        );
        assert_eq!(2, Solution::get_length(ListNode::from(vec![1, 2]).as_ref()));
        assert_eq!(0, Solution::get_length(ListNode::from(vec![]).as_ref()));
        assert_eq!(Solution::is_palindrome(ListNode::from(vec![1])), true);
        assert_eq!(Solution::is_palindrome(ListNode::from(vec![0])), true);
        assert_eq!(Solution::is_palindrome(ListNode::from(vec![1, 2])), false);
        assert_eq!(Solution::is_palindrome(ListNode::from(vec![1, 2, 1])), true);
        assert_eq!(
            Solution::is_palindrome(ListNode::from(vec![1, 2, 2, 1])),
            true
        );
    }
}
fn main() {
    println!("Hello, world!");
}
