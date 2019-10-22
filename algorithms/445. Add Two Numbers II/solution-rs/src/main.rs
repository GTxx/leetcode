
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
    pub fn length(mut list: Option<&Box<ListNode>>) -> i32 {
        let mut i = 0;
        while let Some(node) = list {
            i += 1;
            list = node.next.as_ref();
        }
        i
    }

    pub fn get_nth_mut_ref(
        mut head: Option<&mut Box<ListNode>>,
        n: i32,
    ) -> Option<&mut Box<ListNode>> {
        let mut i = 0;
        while i < n {
            i += 1;
            if let Some(node) = head {
                head = node.next.as_mut();
            } else {
                break;
            }
        }
        head
    }

    pub fn handle_advance(head: Option<&mut Box<ListNode>>) -> bool{
       if let Some(node) = head {
           let advance = Self::handle_advance(node.next.as_mut());
           if advance {
               node.val += 1;
           }
           if node.val >= 10 {
               node.val -= 10;
               true
           } else {
               false
           }
       } else {
           false
       }
    }
    pub fn add_two_numbers(
        l1: Option<Box<ListNode>>,
        l2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let length1 = Self::length(l1.as_ref());
        let length2 = Self::length(l2.as_ref());

        let (mut long, mut short, length, from_n) = if length1 > length2 {
            (l1, l2.as_ref(), length2, length1 - length2)
        } else {
            (l2, l1.as_ref(), length1, length2 - length1)
        };

        let mut nth_ref = Self::get_nth_mut_ref(long.as_mut(), from_n);

        loop {
            match (nth_ref, short) {
                (Some(node), Some(short_node)) => {
                    node.val += short_node.val;
                    nth_ref = node.next.as_mut();
                    short = short_node.next.as_ref()
                }
                _ => break,
            }
        }


        let advance = Self::handle_advance(long.as_mut());
        if advance {
            Some(Box::new(ListNode{val:1, next: long}))
        } else {
            long
        }
    }
}

#[cfg(test)]
mod tests {
    use crate::{ListNode, Solution};

    #[test]
    fn test() {
        assert_eq!(
            Solution::add_two_numbers(ListNode::from(vec![1, 2, 3]), ListNode::from(vec![1, 2, 3])),
            ListNode::from(vec![2, 4, 6])
        );
        assert_eq!(
            Solution::add_two_numbers(ListNode::from(vec![1, 2, 3]), ListNode::from(vec![ 2, 3])),
            ListNode::from(vec![1, 4, 6])
        );
        assert_eq!(
            Solution::add_two_numbers(ListNode::from(vec![2, 3]), ListNode::from(vec![1,2, 3])),
            ListNode::from(vec![1, 4, 6])
        );
        assert_eq!(
            Solution::add_two_numbers(ListNode::from(vec![5, 6]), ListNode::from(vec![1,7, 8])),
            ListNode::from(vec![2, 3, 4])
        );

        assert_eq!(
            Solution::add_two_numbers(ListNode::from(vec![5]), ListNode::from(vec![5])),
            ListNode::from(vec![1, 0])
        );
        assert_eq!(
            Solution::add_two_numbers(ListNode::from(vec![1]), ListNode::from(vec![9,9])),
            ListNode::from(vec![1, 0, 0])
        )

    }
}
fn main() {
    println!("Hello, world!");
}
