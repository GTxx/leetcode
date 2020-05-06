import java.util.Comparator;
import java.util.PriorityQueue;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
  static public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
  }
  public ListNode mergeKLists(ListNode[] lists) {
    PriorityQueue<ListNode> heap = new PriorityQueue<>(Comparator.comparingInt(x -> x.val));
    for (ListNode node: lists) {
      if (node != null) {
        heap.add(node);
      }
    }

    ListNode newHead = new ListNode(0);
    ListNode currentNode = newHead;
    while (!heap.isEmpty()) {
      ListNode node = heap.poll();
      currentNode.next = node;
      currentNode = node;
      if (node.next != null) {
        heap.add(node.next);
      }
    }
    return newHead.next;
  }

  public static ListNode cons(int... arr) {
    ListNode newHead = new ListNode(0);
    ListNode current = newHead;
    for (int i: arr) {
      current.next = new ListNode(i);
      current = current.next;
    }
    return newHead.next;
  }
  public static void main(String[] args) {
//    PriorityQueue<Integer> heap = new PriorityQueue<>();
//    heap.add(2);
//    heap.add(3);
//    heap.add(1);
//    System.out.println(heap.poll());
//    System.out.println(heap.poll());


    ListNode[] list = new ListNode[]{cons(1, 3), cons(2, 4)};
    Solution s = new Solution();
    ListNode newList = s.mergeKLists(list);
    int a = 1;
  }
}