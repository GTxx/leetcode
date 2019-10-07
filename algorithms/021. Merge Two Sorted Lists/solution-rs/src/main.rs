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

    fn from(v: Vec<i32>) -> ListNode {
        let mut result = ListNode::new(0);
        let mut current = &mut result;
        for i in v.iter() {
            let list_node = ListNode::new(*i);
            current = current.next.get_or_insert(Box::new(list_node));
        }
        return *result.next.unwrap();
    }
}

struct Solution;

impl Solution {
    pub fn merge_two_lists(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut result_head = Box::new(ListNode::new(0));
        let mut current_head = &mut result_head;
        let mut l1_current = l1;
        let mut l2_current = l2;


        while l1_current.is_some() && l2_current.is_some() {
            // take content and ownership from l1_current and l2_current, leave l1_current = None, l2_current = None
            let l1_d = l1_current.take();
            let l2_d = l2_current.take();
            if let (Some(mut l1_head), Some(mut l2_head)) = (l1_d, l2_d) {
                if l1_head.val <= l2_head.val {
                    l1_current = l1_head.next.take();
                    // reassign l2_current to get back it's content
                    l2_current = Some(l2_head);
                    current_head = current_head.next.get_or_insert(l1_head);
                } else {
                    l2_current = l2_head.next.take();
                    l1_current = Some(l1_head);
                    current_head = current_head.next.get_or_insert(l2_head);
                }
            }
        }


        // won't work because while let would move l1_current and l2_current, thus both are unavailable after while let
//        while let (Some(l1_head), Some(l2_head)) = (l1_current, l2_current) {
//            if l1_head.val <= l2_head.val {
//                l1_current = l1_head.next.take();
//                l2_current = Some(l2_head);
//                current_head = current_head.next.get_or_insert(l1_current.unwrap());
//            } else {
//                l2_current = l2_head.next.take();
//                l1_current = Some(l1_head);
//                current_head = current_head.next.get_or_insert(l2_current.unwrap());
//            }
//        };
        if l1_current.is_some() {
            current_head.next = l1_current;
        }
        if l2_current.is_some() {
            current_head.next = l2_current;
        }
        return result_head.next;
    }
}

#[cfg(test)]
mod tests {
    use crate::{ListNode, Solution};

    #[test]
    fn test1() {
        let l1 = ListNode::from(vec![1, 2, 3]);
        let l2 = ListNode::from(vec![4, 5, 6]);
        let l3 = Solution::merge_two_lists(Some(Box::new(l1)), Some(Box::new(l2)));
        assert_eq!(l3, Some(Box::new(ListNode::from(vec![1, 2, 3, 4, 5, 6]))));
    }

    #[test]
    fn test_merge_2_empty_list() {
        let l3 = Solution::merge_two_lists(None, None);
        assert_eq!(l3, None);
    }

    #[test]
    fn test3() {
        let l1 = ListNode::from(vec![1, 2, 4]);
        let l2 = ListNode::from(vec![1, 3, 4]);
        let l3 = Solution::merge_two_lists(Some(Box::new(l1)), Some(Box::new(l2)));
        assert_eq!(l3, Some(Box::new(ListNode::from(vec![1, 1, 2, 3, 4, 4]))));
    }
}

fn main() {
    println!("Hello, world!");
}
