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
    fn pop_first(head: Option<Box<ListNode>>) -> (Option<Box<ListNode>>, Option<Box<ListNode>>) {
        if let Some(mut node) = head {
            let next = node.next.take();
            return (Some(node), next);
        } else {
            return (None, None);
        }
    }

    fn get_rest(head: Option<&mut Box<ListNode>>) -> Option<Box<ListNode>> {
        head.and_then(|mut node| node.next.take())
    }

    pub fn swap_pairs(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut new_head = Some(Box::new(ListNode::new(0)));
        let mut new_head_ref = new_head.as_mut();
        let mut rest = head;
        loop {
            let mut rest1 = Self::get_rest(rest.as_mut());
            let first = rest;
            let rest2 = Self::get_rest(rest1.as_mut());
            let second = rest1;
            rest = rest2;
            match (first, second) {
                (Some(first_node), Some(mut second_node)) => {
                    second_node.next = Some(first_node);
                    new_head_ref = new_head_ref.map(|n| {n.next = Some(second_node); n});

                    // get first mut ref
                    new_head_ref = new_head_ref.and_then(|x| x.next.as_mut());
                    // get second mut ref
                    new_head_ref = new_head_ref.and_then(|x| x.next.as_mut());
                },
                (Some(first_node), None) => {
                    new_head_ref = new_head_ref.map(|n| {n.next = Some(first_node); n});
                    break;
                },
                _ => break
            }
        }
        return new_head.unwrap().next;
    }

    pub fn swap_pairs_rec(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        head.map(|mut n| {
            if let Some(mut next_node) = n.next {
                n.next = Self::swap_pairs_rec(next_node.next);
                next_node.next = Some(n);
                return next_node;
            } else {
                return n;
            }
        })
    }

    pub fn swap_pairs_rec1(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        head.and_then(|mut n| {
            match n.next {
                Some(mut m) => {
                    n.next = Solution::swap_pairs_rec1(m.next);
                    m.next = Some(n);
                    Some(m)
                },
                None => Some(n)
            }
        })
    }
}

#[cfg(test)]
mod tests {
    use crate::{ListNode, Solution};

    #[test]
    fn test1() {
        let mut new_l = Solution::swap_pairs(ListNode::from(vec![1, 2, 3, 4]));
        assert_eq!(new_l, ListNode::from(vec![2,1,4,3]));

        new_l = Solution::swap_pairs(ListNode::from(vec![]));
        assert_eq!(new_l, ListNode::from(vec![]));

//        assert_eq!(Solution::swap_pairs(ListNode::from(vec![1])), ListNode::from(vec![1]));
   }

    #[test]
    fn test2() {
        let mut new_l = Solution::swap_pairs_rec(ListNode::from(vec![1, 2, 3, 4]));
        assert_eq!(new_l, ListNode::from(vec![2,1,4,3]));

        new_l = Solution::swap_pairs_rec(ListNode::from(vec![]));
        assert_eq!(new_l, ListNode::from(vec![]));

        assert_eq!(Solution::swap_pairs_rec(ListNode::from(vec![1])), ListNode::from(vec![1]));
    }

    #[test]
    fn test3() {
        let mut new_l = Solution::swap_pairs_rec1(ListNode::from(vec![1, 2, 3, 4]));
        assert_eq!(new_l, ListNode::from(vec![2,1,4,3]));

        new_l = Solution::swap_pairs_rec1(ListNode::from(vec![]));
        assert_eq!(new_l, ListNode::from(vec![]));

        assert_eq!(Solution::swap_pairs_rec1(ListNode::from(vec![1])), ListNode::from(vec![1]));
    }
}
fn main() {
    println!("Hello, world!");
}
