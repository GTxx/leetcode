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
    pub fn length(mut list: Option<&Box<ListNode>>) -> i32 {
        let mut i = 0;
        while let Some(node) = list {
            i += 1;
            list = node.next.as_ref();
        }
        i
    }

    pub fn pop_n(
        list: Option<Box<ListNode>>,
        n: i32,
    ) -> (Option<Box<ListNode>>, Option<Box<ListNode>>) {
        let mut new_head = Some(Box::new(ListNode { val: 0, next: list }));
        let mut mut_head = new_head.as_mut();
        let mut i = 0;
        while let Some(node) = mut_head {
            if i < n {
                i += 1;
                mut_head = node.next.as_mut();
            } else {
                mut_head = Some(node);
                break;
            }
        }
        let rest = mut_head.and_then(|node| node.next.take());
        (new_head.and_then(|mut node| node.next.take()), rest)
    }

    pub fn split_list_to_parts(root: Option<Box<ListNode>>, k: i32) -> Vec<Option<Box<ListNode>>> {
        let mut mut_head = root;
        let mut i = 1;
        let length = Self::length(mut_head.as_ref());
        let num = length / k;
        let first_n = length % k;
        let mut result = vec![];
        for _ in 0..k {
            if i <= first_n {
                let (prev, tail) = Self::pop_n(mut_head, num + 1);
                mut_head = tail;
                result.push(prev);
            } else {
                let (prev, tail) = Self::pop_n(mut_head, num);
                mut_head = tail;
                result.push(prev);
            }
            i += 1;
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
            Solution::split_list_to_parts(ListNode::from(vec![1, 2, 3]), 5),
            vec![
                ListNode::from(vec![1]),
                ListNode::from(vec![2]),
                ListNode::from(vec![3]),
                ListNode::from(vec![]),
                ListNode::from(vec![])
            ]
        );
        assert_eq!(
            Solution::split_list_to_parts(ListNode::from(vec![1, 2, 3,4,5,6,7,8,9,10]), 3),
            vec![
                ListNode::from(vec![1,2,3,4]),
                ListNode::from(vec![5,6,7]),
                ListNode::from(vec![8,9,10])
            ]
        )
    }
}
fn main() {
    println!("Hello, world!");
}
