#[derive(PartialEq, Eq, Clone, Debug)]
 pub struct ListNode {
   pub val: i32,
   pub next: Option<Box<ListNode>>
 }

 impl ListNode {
   #[inline]
   fn new(val: i32) -> Self {
     ListNode {
       next: None,
       val
     }
   }
 }

struct Solution{}

impl Solution {
    pub fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut l1_current = &l1;
        let mut l2_current = &l2;
        let mut result = ListNode::new(0);
        let mut current = &mut result;
        let mut advance = 0;
        loop {
            if let (Some(x), Some(y)) = (l1_current, l2_current) {
                let (list_node, advance1) = Self::make_node(x.val, y.val+advance);
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

    fn make_node(x: i32, y:i32) -> (ListNode, i32){
       if x + y >= 10 {
           (ListNode::new(x + y -10), 1)
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
    use crate::Solution;

    #[test]
    fn test1() {
        assert_eq!(Solution::add_two_numbers(None, None), None)
    }
    #[test]
    fn test2() {
        let list1 = Solution::from(vec![9,8,7]);
        let list2 = Solution::from(vec![2, 2, 2]);
        assert_eq!(*Solution::add_two_numbers(Some(Box::new(list1)), Some(Box::new(list2))).unwrap(), Solution::from(vec![1,1,0,1]))
    }
}
fn main() {
    println!("Hello, world!");
    
}
