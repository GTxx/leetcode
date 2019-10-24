#[derive(PartialEq, Eq, Clone, Debug)]
struct MyLinkedList {
    head: Option<Box<ListNode>>,
    length: i32,
}

#[derive(PartialEq, Eq, Clone, Debug)]
struct ListNode {
    val: i32,
    next: Option<Box<ListNode>>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyLinkedList {
    /** Initialize your data structure here. */
    fn new() -> Self {
        MyLinkedList {
            head: None,
            length: 0,
        }
    }

    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    fn get(&self, index: i32) -> i32 {
        if index + 1 > self.length || index < 0 {
            return -1;
        } else {
            let mut current_node = self.head.as_ref();
            let mut i = 0;
            while let Some(node) = current_node {
                if i == index {
                    return node.val;
                } else {
                    i += 1;
                    current_node = node.next.as_ref();
                }
            }
        }
        -1
    }

    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    fn add_at_head(&mut self, val: i32) {
        if let Some(node) = self.head.take() {
            self.head = Some(Box::new(ListNode {
                val,
                next: Some(node),
            }));;
        } else {
            self.head = Some(Box::new(ListNode { val, next: None }));
        }
        self.length += 1;
    }

    /** Append a node of value val to the last element of the linked list. */
    fn add_at_tail(&mut self, val: i32) {
        let mut current = self.head.as_mut();
        while let Some(node) = current {
            if node.next.is_none() {
                current = Some(node);
                break;
            } else {
                current = node.next.as_mut();
            }
        }
        if let Some(node) = current {
            node.next.replace(Box::new(ListNode { val, next: None }));
        } else {
            self.head.replace(Box::new(ListNode { val, next: None }));
        }
        self.length += 1;
    }

    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    fn add_at_index(&mut self, index: i32, val: i32) {
        if index > self.length {
            return;
        }
        let mut i = 0;
        if index <= 0 {
            self.add_at_head(val);
        }

        let mut current = self.head.as_mut();
        while let Some(node) = current {
            if i + 1 == index {
                current = Some(node);
                break;
            } else {
                i += 1;
                current = node.next.as_mut();
            }
        }

//        println!("{:?}", current);
        if let Some(node) = current {
            let next_node = node.next.take();
            node.next = Some(Box::new(ListNode {
                val,
                next: next_node,
            }))
        }
        self.length += 1;
    }

    /** Delete the index-th node in the linked list, if the index is valid. */
    fn delete_at_index(&mut self, index: i32) {
        if index < 0 || index + 1 > self.length {
            return;
        }

        if index == 0 {
            if let Some(node) = self.head.take() {
                self.head = node.next;
            }
        }

        let mut i = 0;
        let mut current = self.head.as_mut();
        while let Some(node) = current {
            if i + 1 == index {
                current = Some(node);
                break;
            } else {
                current = node.next.as_mut();
                i += 1;
            }
        }

        if let Some(node) = current {
            if let Some(next_node) = node.next.take() {
                node.next = next_node.next;
            }
        }
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * let obj = MyLinkedList::new();
 * let ret_1: i32 = obj.get(index);
 * obj.add_at_head(val);
 * obj.add_at_tail(val);
 * obj.add_at_index(index, val);
 * obj.delete_at_index(index);
 */

#[cfg(test)]
mod tests {
    use crate::MyLinkedList;

    #[test]
    fn test() {
        let mut obj = MyLinkedList::new();
        assert_eq!(obj.get(1), -1);
        assert_eq!(obj.get(0), -1);
        obj.add_at_head(1);
        obj.add_at_tail(3);
        obj.add_at_index(1, 2);
        println!("{:?}", obj);
        assert_eq!(obj.get(1), 2);
        obj.delete_at_index(0);
        assert_eq!(obj.get(0), 2);
    }

    #[test]
    fn test1() {
        //        ["MyLinkedList","addAtHead","addAtIndex","get","get","get"]
        //        [[],[1],[1,2],[1],[0],[2]]
        let mut obj = MyLinkedList::new();
        obj.add_at_head(1);
        obj.add_at_index(1, 2);
        assert_eq!(obj.get(1), 2);
        assert_eq!(obj.get(0), 1);
        assert_eq!(obj.get(2), -1);
    }

    #[test]
    fn test2() {
        //        ["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
        //        [[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]

        let mut obj = MyLinkedList::new();
        obj.add_at_head(7);
        obj.add_at_head(2);
        obj.add_at_head(1);
        obj.add_at_index(3, 0);
        println!("{:?}", obj);
        obj.delete_at_index(2);
        obj.add_at_head(6);
        obj.add_at_tail(4);
        println!("{:?}", obj);
        assert_eq!(obj.get(4), 4);
        obj.add_at_head(4);
        obj.add_at_index(5, 0);
        obj.add_at_head(6);
    }

    #[test]
    fn test3() {
//        ["MyLinkedList","addAtIndex","get","deleteAtIndex"]
//        [[],[-1,0],[0],[-1]]
        let mut obj = MyLinkedList::new();
        obj.add_at_index(-1, 0);
        assert_eq!(obj.get(0), 0);
        obj.delete_at_index(-1);
    }

    #[test]
    fn test4() {
        let mut obj = MyLinkedList::new();
        obj.add_at_head(56);
        println!("{:?}", obj);
        obj.add_at_index(1, 50);
        println!("{:?}", obj);
        obj.delete_at_index(1);
        println!("{:?}", obj);
        assert_eq!(obj.get(1), -1);
    }
}
fn main() {
    println!("Hello, world!");
}
