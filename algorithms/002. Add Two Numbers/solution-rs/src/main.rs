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
    // init list from vector
    fn from(v: Vec<i32>) -> Option<Box<ListNode>> {
        let mut head = Box::new(Self::new(0));
        let mut head_ref = &mut head;
        for i in v {
            head_ref = head_ref.next.get_or_insert(Box::new(ListNode::new(i)));
        }
        head.next
    }
}

pub fn reverse(list: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    unimplemented!();
}

pub fn pop(list: Option<Box<ListNode>>) -> (Option<Box<ListNode>>, Option<Box<ListNode>>) {
    if let Some(mut node) = list {
        let tail = node.next.take();
        (Some(node), tail)
    } else {
        (None, None)
    }
}

pub fn pop_n(
    list: Option<Box<ListNode>>,
    n: i32,
) -> (Option<Box<ListNode>>, Option<Box<ListNode>>) {
    let mut new_head = Some(Box::new(ListNode { val: 0, next: list }));
    let mut mut_head = new_head.as_mut();
    let mut i = 0;
    while let Some(node) = mut_head {
        if i < n {
            i += 1;
            mut_head = node.next.as_mut();
        } else {
            mut_head = Some(node);
            break;
        }
    }
    let rest = mut_head.and_then(|node| node.next.take());
    (
        new_head.and_then(|mut node| node.next.take()),
        rest
    )
}

pub fn split_n(list: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    unimplemented!()
}

pub fn length(mut list: Option<&Box<ListNode>>) -> i32 {
    let mut i = 0;
    while let Some(node) = list {
        i += 1;
        list = node.next.as_ref();
    }
    i
}

pub fn get_nth_mut_ref(mut head: Option<&mut Box<ListNode>>, n: i32) -> Option<&mut Box<ListNode>> {
    let mut i = 0;
    while i < n {
        i += 1;
        if let Some(node) = head {
            head = node.next.as_mut();
        } else {
            break;
        }
    }
    println!("head now is {:?}", head);
    head
}

struct Solution;

impl Solution {
    pub fn add_two_numbers(
        l1: Option<Box<ListNode>>,
        l2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut l1_current = &l1;
        let mut l2_current = &l2;
        let mut result = ListNode::new(0);
        let mut current = &mut result;
        let mut advance = 0;
        loop {
            if let (Some(x), Some(y)) = (l1_current, l2_current) {
                let (list_node, advance1) = Self::make_node(x.val, y.val + advance);
                advance = advance1;
                current = current.next.get_or_insert(Box::new(list_node));
                l1_current = &x.next;
                l2_current = &y.next;
            } else if let Some(y1) = l2_current {
                let (list_node, advance1) = Self::make_node(0, y1.val + advance);
                advance = advance1;
                current = current.next.get_or_insert(Box::new(list_node));
                l2_current = &y1.next;
            } else if let Some(x) = l1_current {
                let (list_node, advance1) = Self::make_node(x.val, advance);
                advance = advance1;
                current = current.next.get_or_insert(Box::new(list_node));
                l1_current = &x.next;
            } else {
                break;
            }
        }
        if advance == 1 {
            current.next.replace(Box::new(ListNode::new(1)));
        }
        return result.next;
    }

    fn make_node(x: i32, y: i32) -> (ListNode, i32) {
        if x + y >= 10 {
            (ListNode::new(x + y - 10), 1)
        } else {
            (ListNode::new(x + y), 0)
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
#[cfg(test)]
mod tests {
    use crate::{get_nth_mut_ref, length, ListNode, Solution, pop, pop_n};

    #[test]
    fn test() {
        println!("{:?}", ListNode::from(vec![1, 2, 3]));
        assert_eq!(ListNode::from(vec![1, 2, 3]).as_ref().unwrap().val, 1);
        assert_eq!(length(ListNode::from(vec![]).as_ref()), 0);
        assert_eq!(length(ListNode::from(vec![1, 2, 3]).as_ref()), 3);
        assert_eq!(
            get_nth_mut_ref(ListNode::from(vec![1, 2, 3]).as_mut(), 1)
                .unwrap()
                .val,
            2
        );

        assert_eq!(
            get_nth_mut_ref(ListNode::from(vec![1, 2, 3]).as_mut(), 0)
                .unwrap()
                .val,
            1
        );

        assert_eq!(
            get_nth_mut_ref(ListNode::from(vec![1, 2, 3]).as_mut(), 2)
                .unwrap()
                .val,
            3
        );

        assert_eq!(
            get_nth_mut_ref(ListNode::from(vec![1, 2, 3]).as_mut(), 4),
            None
        );

        assert_eq!(pop(ListNode::from(vec![1,2,3])), (ListNode::from(vec![1]), ListNode::from(vec![2,3])));
        assert_eq!(pop(ListNode::from(vec![])), (None, None));

        assert_eq!(pop_n(ListNode::from(vec![1,2]), 1), (ListNode::from(vec![1]), ListNode::from(vec![2])));
        assert_eq!(pop_n(ListNode::from(vec![1,2]), 0), (None, ListNode::from(vec![1, 2])));
        assert_eq!(pop_n(ListNode::from(vec![1,2]), 2), (ListNode::from(vec![1, 2]), None));
        assert_eq!(pop_n(ListNode::from(vec![1,2]), 3), (ListNode::from(vec![1, 2]), None));
    }
    #[test]
    fn test1() {
        assert_eq!(Solution::add_two_numbers(None, None), None)
    }
    #[test]
    fn test2() {
        let list1 = Solution::from(vec![9, 8, 7]);
        let list2 = Solution::from(vec![2, 2, 2]);
        assert_eq!(
            *Solution::add_two_numbers(Some(Box::new(list1)), Some(Box::new(list2))).unwrap(),
            Solution::from(vec![1, 1, 0, 1])
        )
    }
}
fn main() {
    println!("Hello, world!");
}
