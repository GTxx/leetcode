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
    pub fn odd_even_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut mut_head = head;
        let mut mut_head_ref = mut_head.as_mut();
        let mut even_head = Some(Box::new(ListNode::new(1)));
        let mut even_ref = even_head.as_mut();

        while let Some(node_prev) = mut_head_ref {
            let mut even = node_prev.next.take();
            let odd = even.as_mut().and_then(|node| node.next.take());

            // append even node to even list
            if let Some(node) = even_ref {
                node.next = even;
                even_ref = node.next.as_mut();
            }

            // append odd node to odd list
            node_prev.next = odd;
            if node_prev.next.is_some() {
                mut_head_ref = node_prev.next.as_mut();
            } else {
                mut_head_ref = Some(node_prev);
                break;
            }
        }

        if let (Some(node), Some(even_node)) = (mut_head_ref, even_head) {
            node.next = even_node.next;
        }

        mut_head
    }
}

#[cfg(test)]
mod tests {
    use crate::{ListNode, Solution};

    #[test]
    fn test() {
        assert_eq!(
            Solution::odd_even_list(ListNode::from(vec![1, 2, 3, 4, 5])),
            ListNode::from(vec![1, 3, 5, 2, 4])
        );
        assert_eq!(
            Solution::odd_even_list(ListNode::from(vec![])),
            ListNode::from(vec![])
        );
        assert_eq!(
            Solution::odd_even_list(ListNode::from(vec![1, 2, 3, 4])),
            ListNode::from(vec![1, 3, 2, 4])
        );
    }

}
fn main() {
    println!("Hello, world!");
}
