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
    pub fn get_n_th_node(
        head: Option<Box<ListNode>>,
        m: i32,
    ) -> (Option<Box<ListNode>>, Option<Box<ListNode>>) {
        let mut new_head = Some(Box::new(ListNode { val: 0, next: head }));
        let mut new_head_ref = new_head.as_mut();
        let mut i = 0;
        let mut result = None;
        while let Some(node) = new_head_ref {
            i += 1;
            if i >= m {
                result = node.next.take();
                break;
            } else {
                new_head_ref = node.next.as_mut();
            }
        }
        return (new_head.unwrap().next, result);
    }

    pub fn append(
        first: Option<Box<ListNode>>,
        second: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut first_mut = first;
        let first_tail = first_mut.as_mut().map(|mut node| {
            while let Some(next_node) = node.next.take() {
                if next_node.next.is_some() {
                    node = node.next.get_or_insert(next_node);
                    continue;
                } else {
                    node = node.next.get_or_insert(next_node);
                    break;
                }
            }
            return node;
        });
        if let Some(node) = first_tail {
            node.next = second;
            return first_mut;
        } else {
            return second;
        }
    }

    pub fn reverse_first_n(head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {
        let mut current = head;
        let mut j = 0;
        let mut tail = None;
        while let Some(mut x) = current {
            if j <= n {
                let next = x.next.take();
                x.next = tail;
                tail = Some(x);
                current = next;
            } else {
                tail = Self::append(tail, Some(x));
                break;
            }
            j += 1;
        }
        tail
    }

    pub fn reverse_between(head: Option<Box<ListNode>>, m: i32, n: i32) -> Option<Box<ListNode>> {
        // get m th node
        let (first, mut second) = Self::split_n(head, m);

//        println!("{:?}", second);
        // reverse from m th node to n th node
        second = Self::reverse_first_n(second, n - m);

        // append first and second
        Self::append(first, second)
    }

    // return first head, first tail mutable reference, second head
    pub fn split_n(
        head: Option<Box<ListNode>>,
        n: i32,
    ) -> (Option<Box<ListNode>>, Option<Box<ListNode>>) {
        if n == 1 {
            return (None, head);
        }
        let mut mut_head = head;
        let mut current = mut_head.as_mut();
        let mut j = 1;
        while let Some(mut node) = current {
            if j < n - 1 {
                current = node.next.as_mut();
                j += 1;
            } else {
                current = Some(node);
                break;
            }
        }
        let second = current.and_then(|node| node.next.take());
        return (mut_head, second);
    }
}

#[cfg(test)]
mod tests {
    use crate::{ListNode, Solution};

    #[test]
    fn test() {
        assert_eq!(
            Solution::get_n_th_node(ListNode::from(vec![1, 2]), 2),
            (ListNode::from(vec![1]), ListNode::from(vec![2]))
        );
    }

    #[test]
    fn test1() {
        assert_eq!(
            Solution::append(ListNode::from(vec![1]), ListNode::from(vec![2])),
            ListNode::from(vec![1, 2])
        );
        assert_eq!(
            Solution::append(ListNode::from(vec![]), ListNode::from(vec![2])),
            ListNode::from(vec![2])
        );
        assert_eq!(
            Solution::append(ListNode::from(vec![1]), ListNode::from(vec![])),
            ListNode::from(vec![1])
        );
    }

    #[test]
    fn test2() {
        assert_eq!(
            Solution::reverse_first_n(ListNode::from(vec![1, 2, 3]), 2),
            ListNode::from(vec![2, 1, 3])
        );
        panic!()
    }
    #[test]
    fn test3() {
        assert_eq!(
            Solution::reverse_between(ListNode::from(vec![1, 2, 3, 4, 5]), 2, 4),
            ListNode::from(vec![1, 4, 3, 2, 5])
        );
        assert_eq!(
        Solution::reverse_between(ListNode::from(vec![3,5]), 1, 2),
        ListNode::from(vec![5,3])
        )
    }
}
fn main() {
    println!("Hello, world!");
}
