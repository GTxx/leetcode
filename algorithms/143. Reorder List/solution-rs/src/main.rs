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
        let mut new_head = ListNode::new(0);
        let mut current = &mut new_head;
        for i in v {
            current = current.next.get_or_insert(Box::new(ListNode::new(i)));
        }
        return new_head.next;
    }
}
struct Solution;
impl Solution {
    pub fn split_n(head: Option<&mut Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {
        let mut head_mut = head;
        let mut i = 1;
        while let Some(node) = head_mut {
            if i < n {
                head_mut = node.next.as_mut();
            } else {
                head_mut = Some(node);
                break;
            }
            i += 1;
        }
        return head_mut.and_then(|node| node.next.take());
    }

    pub fn reverse(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut tail = None;
        let mut mut_head = head;
        while let Some(mut node) = mut_head {
            mut_head = node.next.take();
            node.next = tail;
            tail = Some(node);
        }
        tail
    }

    pub fn reorder_list(head: &mut Option<Box<ListNode>>) {
        let mut ref_head = head.as_ref();
        let mut length = 0;
        while let Some(node) = ref_head {
            length += 1;
            ref_head = node.next.as_ref();
        }

        let n = (length + 1) / 2;
        let mut second = Self::split_n(head.as_mut(), n);
        second = Self::reverse(second);

        if let Some(node) = head {
            let first = node.next.take();
            let tail = Self::merge_iter(second, first);
            node.next = tail;
        }
    }

    pub fn merge(
        first: Option<Box<ListNode>>,
        second: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>>{
        match (first, second) {
            (Some(mut node1), Some(mut node2)) => {
                let node1_next = node1.next.take();
                let tail = Self::merge(node1_next, node2.next.take());
                node2.next = tail;
                node1.next = Some(node2);
                Some(node1)
            },
            (None, None) => None,
            (Some(node), None) | (None, Some(node)) => Some(node),
        }
    }

    pub fn merge_iter(
        first: Option<Box<ListNode>>,
        second: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut new_head = Some(Box::new(ListNode::new(0)));
        let mut prev_ref = new_head.as_mut();
        let mut mut_first = first;
        let mut mut_second = second;
        loop {
            match (mut_first, mut_second) {
                (None, None) => {
                    break;
                },
                (None, Some(node)) | (Some(node), None) => {
                    if let Some(prev_node) = prev_ref {
                        prev_node.next = Some(node);
                    }
                    break;
                },
                (Some(mut node1), Some(mut node2)) => {
                    mut_first = node1.next.take();
                    mut_second = node2.next.take();
                    if let Some(prev_node) = prev_ref {
                        node1.next = Some(node2);
                        prev_node.next = Some(node1);
                        prev_ref = Self::get_nth_mut_ref(Some(prev_node), 2);
                    }
                }
            }
        }
        new_head.and_then(|mut node| node.next.take())
    }

    pub fn get_nth_mut_ref(head: Option<&mut Box<ListNode>>, n: i32) -> Option<&mut Box<ListNode>> {
        let mut mut_ref = head;
        let mut i = 0;
        while i < n {
            i += 1;
            if let Some(ref_node) = mut_ref.take() {
                mut_ref = ref_node.next.as_mut();
            } else {
                break;
            }
        }
        return mut_ref;
    }
}

#[cfg(test)]
mod tests {
    use crate::{ListNode, Solution};

    #[test]
    fn test() {
        let mut l = ListNode::from(vec![1, 2, 3, 4]);
        Solution::reorder_list(&mut l);
        assert_eq!(l, ListNode::from(vec![1, 4, 2, 3]));

        l = ListNode::from(vec![]);
        Solution::reorder_list(&mut l);
        assert_eq!(l, ListNode::from(vec![]));

        l = ListNode::from(vec![1,2]);
        Solution::reorder_list(&mut l);
        assert_eq!(l, ListNode::from(vec![1,2]));

        l = ListNode::from(vec![1,2,3]);
        Solution::reorder_list(&mut l);
        assert_eq!(l, ListNode::from(vec![1,3,2]));
    }

    #[test]
    fn test1() {
        let mut l = ListNode::from(vec![1,2,3,4]);
        let mut_ref = Solution::get_nth_mut_ref(l.as_mut(), 2);
        println!("{:?}", mut_ref);
        panic!("123");
    }
}
fn main() {
    println!("Hello, world!");
}
