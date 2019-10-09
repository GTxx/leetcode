// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode {
            next: None,
            val,
        }
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

    fn take_first(self) -> (Option<Box<List>>, Option<Box<List>>) {
       unimplemented!()
    }
}

struct Solution;

impl Solution {
    pub fn remove_elements(head: Option<Box<ListNode>>, val: i32) -> Option<Box<ListNode>> {
        head.and_then(|mut node| {
            if node.val == val {
                 Solution::remove_elements(node.next, val)
            } else {
                node.next = Self::remove_elements(node.next.take(), val);
                Some(node)
            }
        })
    }
}

#[cfg(test)]
mod tests {
    use crate::{Solution, ListNode};

    #[test]
    fn test() {
        assert_eq!(ListNode::from(vec![1,2]), Solution::remove_elements(ListNode::from(vec![1,2,3]), 3));

        assert_eq!(ListNode::from(vec![]), Solution::remove_elements(ListNode::from(vec![]), 3));

        assert_eq!(ListNode::from(vec![1,2,3,4,5]), Solution::remove_elements(ListNode::from(vec![1,2,6,3,4,5,6]), 6));
    }
}

fn main() {
    println!("Hello, world!");
}
