use std::borrow::BorrowMut;

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
    pub fn remove_nth_from_end(head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {

        let length = Self::get_list_len(&head);
        let mut new_node = ListNode::new(0);
        new_node.next = head;

        let mut current_node = &mut new_node;
        let mut nth = 0;
        while nth < length - n && current_node.next.is_some() {
            current_node = current_node.next.as_mut().unwrap();
            nth += 1;
        }
        current_node.next.take().map(|next_node| current_node.next = next_node.next);
        return new_node.next;
    }

    pub fn get_list_len(head: &Option<Box<ListNode>>) -> i32{
        let mut current = head.as_ref();
        let mut length = 0;
        while let Some(p) = current {
            length += 1;
            current = p.next.as_ref();
        }
        return length;
    }
}

#[cfg(test)]
mod tests {
    use crate::{ListNode, Solution};

    #[test]
    fn test () {
        let l1 = ListNode::from(vec![1,2,3]);
        let l2 = ListNode::from(vec![1,2,3]);
        let l3 = ListNode::from(vec![1,2,3,4]);

        assert_eq!(l1, l2);
        assert_ne!(l1, l3);
    }
    #[test]
    fn test1() {
        let mut l = ListNode::from(vec![1, 2, 3, 4, 5]);
        l = Solution::remove_nth_from_end(l, 2);
        assert_eq!(l, ListNode::from(vec![1,2,3,5]))
    }

    #[test]
    fn test2() {
        let mut l = ListNode::from(vec![1]);
        l = Solution::remove_nth_from_end(l, 1);
        assert_eq!(l, ListNode::from(vec![]))
    }
}

fn main() {
    println!("Hello, world!");
}
