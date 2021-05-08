use std::{cell::RefCell, cmp, rc::Rc};

// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}
struct Solution;
fn get_min(root: Option<Rc<RefCell<TreeNode>>>) -> Option<i32> {
    if let Some(r) = root {
        if let Some(left) = r.borrow().left.clone() {
            return get_min(Some(left));
        } else {
            return Some(r.borrow().val);
        }
    } else {
        None
    }
}

fn get_max(root: Option<Rc<RefCell<TreeNode>>>) -> Option<i32> {
    if let Some(r) = root {
        if let Some(right) = r.borrow().right.clone() {
            return get_max(Some(right));
        } else {
            return Some(r.borrow().val);
        }
    } else {
        None
    }
}
pub fn get_minimum_difference(root: Option<Rc<RefCell<TreeNode>>>) -> Option<i32> {
    if let Some(r) = root {
        let left_max = get_max(r.borrow().left.clone());
        let right_min = get_min(r.borrow().right.clone());
        let root_left_diff = left_max.map(|v| r.borrow().val - v);
        let root_right_diff = right_min.map(|v| v - r.borrow().val);
        let left_diff = get_minimum_difference(r.borrow().left.clone());
        let right_diff = get_minimum_difference(r.borrow().right.clone());
        let x = vec![root_left_diff, root_right_diff, left_diff, right_diff]
            .into_iter()
            .fold(None, |a, b| match (a, b) {
                (Some(x), Some(y)) => Some(cmp::min(x, y)),
                (Some(x), None) => Some(x),
                (None, Some(y)) => Some(y),
                (None, None) => None,
            });
        x.map(|i| i.to_owned())
    } else {
        None
    }
}
impl Solution {
    pub fn get_minimum_difference(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        get_minimum_difference(root).unwrap()
    }
}

fn main() {
    let mut root = TreeNode::new(4);
    let mut left = TreeNode::new(2);
    let right = TreeNode::new(6);
    let left1 = TreeNode::new(1);
    let left2 = TreeNode::new(3);
    left.left = Some(Rc::new(RefCell::new(left1)));
    left.right = Some(Rc::new(RefCell::new(left2)));
    root.left = Some(Rc::new(RefCell::new(left)));
    root.right = Some(Rc::new(RefCell::new(right)));
    assert_eq!(
        Solution::get_minimum_difference(Some(Rc::new(RefCell::new(root)))),
        1
    );
}
