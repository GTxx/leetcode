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
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut tail = None;
        let mut mut_head = head;
        while let Some(mut mut_head_ref) = mut_head.take() {
            let next = mut_head_ref.next.take();
            mut_head_ref.next = tail;
            tail = Some(mut_head_ref);
            mut_head = next;
        }
        return tail;
    }
}

#[cfg(test)]
mod tests {
    use crate::{ListNode, Solution};

    #[test]
   fn test1() {
        assert_eq!(ListNode::from(vec![]), Solution::reverse_list(ListNode::from(vec![])));

        assert_eq!(ListNode::from(vec![1]), Solution::reverse_list(ListNode::from(vec![1])));
        assert_eq!(ListNode::from(vec![1,2]), Solution::reverse_list(ListNode::from(vec![2,1])));
   }
}
fn main() {
    println!("Hello, world!");
}
