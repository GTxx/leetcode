use std::thread::current;

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
    fn get_rest(head: Option<&mut Box<ListNode>>) -> Option<Box<ListNode>> {
        head.and_then(|mut node| node.next.take())
    }

    fn reverse(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut reversed_list = None;
        let mut current_head = head;
        while let Some(mut current_head_p) = current_head.take() {
            current_head = current_head_p.next.take();
            current_head_p.next = reversed_list;
            reversed_list = Some(current_head_p);
        }
        return reversed_list;
    }
    fn get_rest_n(head: Option<&mut Box<ListNode>>, skip: i32) -> Option<Box<ListNode>> {
        let mut n1 = skip;
        let mut new_head = head;
        while n1 > 1 {
            n1 -= 1;
            if let Some(mut new_head_ref) = new_head {
                new_head = new_head_ref.next.as_mut();
            } else {
                return None;
            }
        }
        return new_head.and_then(|mut node| node.next.take());
    }

    fn get_len(head: Option<&Box<ListNode>>) -> i32 {
        let mut mut_head = head;
        let mut i = 0;
        while let Some(p) = mut_head {
            i += 1;
            mut_head = p.next.as_ref();
        }
        return i;
    }

    pub fn append(
        head1: Option<Box<ListNode>>,
        head2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut mut_head1 = head1;
        let mut mut_head1_ref = mut_head1.as_mut();

        while let Some(p) = mut_head1_ref {
            if p.next.is_some() {
                mut_head1_ref = p.next.as_mut();
            } else {
                p.next = head2;
                break;
            }
        }
        return mut_head1;
    }

    pub fn reverse_first_n(
        head: Option<Box<ListNode>>,
        k: i32,
    ) -> (Option<Box<ListNode>>, Option<Box<ListNode>>) {
        if Self::get_len(head.as_ref()) < k {
            return (head, None);
        }
        let mut reversed_list = None;
        let mut current_head = head;
        let mut i = 0;
        let mut skip_k_head = None;
        while let Some(mut current_head_p) = current_head.take() {
            i += 1;
            if i < k {
                current_head = current_head_p.next.take();
                current_head_p.next = reversed_list;
                reversed_list = Some(current_head_p);
            } else {
                skip_k_head = current_head_p.next.take();
                current_head_p.next = reversed_list;
                reversed_list = Some(current_head_p);
                break;
            }
        }
        return (reversed_list, skip_k_head);
    }
    pub fn reverse_k_group(head: Option<Box<ListNode>>, k: i32) -> Option<Box<ListNode>> {
        let (first_list, rest_list) = Self::reverse_first_n(head, k);
        if rest_list.is_none() {
            return first_list;
        } else {
            return Self::append(first_list, Self::reverse_k_group(rest_list, k));
        }
    }
}

mod tests {
    use crate::{ListNode, Solution};

    #[test]
    fn test1() {
        let mut l = ListNode::from(vec![1, 2, 3, 4]);
        assert_eq!(
            Solution::get_rest_n(l.as_mut(), 2),
            ListNode::from(vec![3, 4])
        );
        assert_eq!(l, ListNode::from(vec![1, 2]));

        let mut l1 = ListNode::from(vec![1, 2]);
        assert_eq!(Solution::get_rest_n(l1.as_mut(), 3), ListNode::from(vec![]));
        assert_eq!(l1, ListNode::from(vec![1, 2]));
    }

    #[test]
    fn test2() {
        assert_eq!(
            ListNode::from(vec![1, 2, 3]),
            Solution::reverse(ListNode::from(vec![3, 2, 1]))
        );
        assert_eq!(
            ListNode::from(vec![]),
            Solution::reverse(ListNode::from(vec![]))
        );
        assert_eq!(
            ListNode::from(vec![1]),
            Solution::reverse(ListNode::from(vec![1]))
        );
    }

    #[test]
    fn test3() {
        assert_eq!(
            Solution::reverse_first_n(ListNode::from(vec![1, 2, 3]), 2),
            (ListNode::from(vec![2, 1]), ListNode::from(vec![3]))
        );
    }

    #[test]
    fn test4() {
        assert_eq!(
            Solution::append(ListNode::from(vec![1]), ListNode::from(vec![2])),
            ListNode::from(vec![1, 2])
        );
    }

    #[test]
    fn test5() {
        assert_eq!(
            Solution::reverse_k_group(ListNode::from(vec![1, 2, 3, 4, 5]), 2),
            ListNode::from(vec![2, 1, 4, 3, 5])
        );
        assert_eq!(
            Solution::reverse_k_group(ListNode::from(vec![1, 2, 3, 4, 5]), 3),
            ListNode::from(vec![3, 2, 1, 4, 5])
        )
    }
}

fn main() {
    println!("Hello, world!");
}
