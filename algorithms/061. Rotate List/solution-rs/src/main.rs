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
    pub fn rotate_right(head: Option<Box<ListNode>>, k: i32) -> Option<Box<ListNode>> {
        if head.is_none() {
            return None;
        }
        // get list length
        let mut length = 0;
        let mut mut_head = head;
        let mut head_ref: Option<&Box<ListNode>> = mut_head.as_ref();
        while let Some(x) = head_ref {
            length += 1;
            head_ref = x.next.as_ref();
        }

        // rotate
        let real_shift = k % length;
        if real_shift == 0 {
            return mut_head;
        } else {
            let mut j = 0;
            let mut head_mut_ref = mut_head.as_mut();
            let mut real_head = None;
            while let Some(x) = head_mut_ref.take() {
                j += 1;
                if j < length - real_shift {
                    head_mut_ref = x.next.as_mut();
                    continue;
                } else {
                    head_mut_ref = Some(x);
                    break;
                }
            }
            if let Some(x) = head_mut_ref {
                real_head = x.next.take();
                head_mut_ref = Some(x);
            }

            let mut node_ref = real_head.as_mut();
            // get tail
            while let Some(x) = node_ref {
                if x.next.is_none() {
                    node_ref = Some(x);
                    break;
                } else {
                    node_ref = x.next.as_mut();
                }
            }
            node_ref.map(|node| node.next = mut_head);
            return real_head;
        }
    }
}

#[cfg(test)]
mod tests {
    use crate::{ListNode, Solution};

    #[test]
    fn test() {
        assert_eq!(
            ListNode::from(vec![1, 2]),
            Solution::rotate_right(ListNode::from(vec![1, 2]), 2)
        );
        assert_eq!(
            ListNode::from(vec![3, 1, 2]),
            Solution::rotate_right(ListNode::from(vec![1, 2, 3]), 1)
        );
        assert_eq!(
            ListNode::from(vec![2, 3, 1]),
            Solution::rotate_right(ListNode::from(vec![1, 2, 3]), 2)
        );
        assert_eq!(
            ListNode::from(vec![4, 5, 1, 2, 3]),
            Solution::rotate_right(ListNode::from(vec![1, 2, 3, 4, 5]), 2)
        );
    }

}
fn main() {
    println!("Hello, world!");
}
