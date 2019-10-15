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
    pub fn middle_node(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut new_head = Some(Box::new(ListNode {
            val:0, next: head
        }));
        let mut length = 0;
        let mut head_ref = new_head.as_ref();
        while let Some(p) = head_ref {
            length += 1;
            head_ref = p.next.as_ref();
        }

        let mut middle = if length % 2 == 1 {  (length + 1) /2 } else {length / 2 };
        let mut mut_head_ref = new_head.as_mut();
        while middle > 1 {
            middle -= 1;
            if let Some(p) = mut_head_ref {
                mut_head_ref = p.next.as_mut();
            }
        }
        return mut_head_ref.and_then(|p| p.next.take());
    }
}

#[cfg(test)]
mod tests {
    use crate::{Solution, ListNode};

    #[test]
    fn test1() {
        assert_eq!(Solution::middle_node(ListNode::from(vec![1])), ListNode::from(vec![1]));
        assert_eq!(Solution::middle_node(ListNode::from(vec![1,2,3])), ListNode::from(vec![2,3]));
        assert_eq!(Solution::middle_node(ListNode::from(vec![1,2,3,4,5,6])), ListNode::from(vec![4,5,6]));
    }
}
fn main() {
    println!("Hello, world!");
}
