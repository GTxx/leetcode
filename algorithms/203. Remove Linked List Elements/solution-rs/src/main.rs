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
}

struct Solution;

impl Solution {
    fn take_first(head: Option<Box<ListNode>>) -> (Option<Box<ListNode>>, Option<Box<ListNode>>) {
        if let Some(mut node) = head {
            let next = node.next.take();
            return (Some(node), next);
        } else {
            return (None, None);
        }
    }

    fn take_first_n(head: Option<Box<ListNode>>, n: i32) -> (Vec<Option<Box<ListNode>>>, Option<Box<ListNode>>) {
        let mut i = 0;
        let mut first_n = vec![];
        let mut head_p = head;
        while i < n {
            i += 1;
            if let Some(mut node) = head_p {
                let next = node.next.take();
                first_n.push(Some(node));
                head_p = next;
            } else {
                break;
            }
        }
        return (first_n, head_p);
    }

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

    pub fn remove_elements_iter(head: Option<Box<ListNode>>, val: i32) -> Option<Box<ListNode>> {
        let mut new_head = Some(Box::new(ListNode::new(0)));
        let mut current_head = &mut new_head;
        let mut rest = head;
        loop {
            let (first, rest1) = Self::take_first(rest);
            rest = rest1;
            if let Some(node) = first {
                if node.val != val {
                    if let Some(n) = current_head {
                        n.next = Some(node);
                        current_head = &mut n.next;
                    }
                }
            } else {
                break;
            }
        }
        return new_head.unwrap().next;
    }
}


#[cfg(test)]
mod tests {
    use crate::{Solution, ListNode};

    #[test]
    fn base_test() {
        let (first, rest) = Solution::take_first(ListNode::from(vec![1, 2]));
        assert_eq!(first, Some(Box::new(ListNode::new(1))));
        assert_eq!(rest, ListNode::from(vec![2]));

        let (first, rest) = Solution::take_first(ListNode::from(vec![]));
        assert_eq!(first, None);
        assert_eq!(rest, ListNode::from(vec![]));

        let (first_n, rest) = Solution::take_first_n(ListNode::from(vec![1, 2]), 0);
        assert_eq!(first_n, vec![]);
        assert_eq!(rest, ListNode::from(vec![1, 2]));

        let (first_n, rest) = Solution::take_first_n(ListNode::from(vec![1, 2]), 1);
        assert_eq!(first_n, vec![Some(Box::new(ListNode::new(1)))]);
        assert_eq!(rest, ListNode::from(vec![2]));

        let (first_n, rest) = Solution::take_first_n(ListNode::from(vec![1, 2]), 3);
        assert_eq!(first_n, vec![Some(Box::new(ListNode::new(1))), Some(Box::new(ListNode::new(2)))]);
        assert_eq!(rest, ListNode::from(vec![]));
    }

    #[test]
    fn test() {
        assert_eq!(ListNode::from(vec![1, 2]), Solution::remove_elements(ListNode::from(vec![1, 2, 3]), 3));

        assert_eq!(ListNode::from(vec![]), Solution::remove_elements(ListNode::from(vec![]), 3));

        assert_eq!(ListNode::from(vec![1, 2, 3, 4, 5]), Solution::remove_elements(ListNode::from(vec![1, 2, 6, 3, 4, 5, 6]), 6));
    }

    #[test]
    fn test1 () {
        assert_eq!(ListNode::from(vec![1, 2]), Solution::remove_elements_iter(ListNode::from(vec![1, 2, 3]), 3));
        assert_eq!(ListNode::from(vec![]), Solution::remove_elements_iter(ListNode::from(vec![]), 3));
        assert_eq!(ListNode::from(vec![1, 2, 3, 4, 5]), Solution::remove_elements_iter(ListNode::from(vec![1, 2, 6, 3, 4, 5, 6]), 6));
    }
}

fn main() {
    println!("Hello, world!");
}
