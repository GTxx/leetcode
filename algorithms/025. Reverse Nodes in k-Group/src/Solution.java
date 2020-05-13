/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    static public class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

    class Result {
        public ListNode preList;
        public ListNode nextList;
        public int preLen;
    }

    public Result takeFirstK(ListNode head, int k) {
        if (head == null) {
            Result result = new Result();
            result.preLen = 0;
            result.preList = null;
            result.nextList = null;
            return result;
        }
        int i = 0;
        ListNode current = head;
        while (i < k - 1 && current.next != null) {
            current = current.next;
            i += 1;
        }
        ListNode nextList = current.next;
        current.next = null;

        Result result = new Result();
        result.preList = head;
        result.nextList = nextList;
        result.preLen = i + 1;
        return result;
    }

    public ListNode reverse(ListNode head) {
        if (head == null) return null;
        ListNode newList = head;
        ListNode rest = head.next;
        head.next = null;
        while (rest != null) {
            ListNode current = rest;
            rest = rest.next;
            current.next = newList;
            newList = current;
        }
        return newList;
    }

    public ListNode concat(ListNode l1, ListNode l2) {
        if (l1 == null) return l2;
        if (l2 == null) return l1;
        ListNode newHead = new ListNode();
        newHead.next = l1;
        while (l1.next != null) {
            l1 = l1.next;
        }
        l1.next = l2;
        return newHead.next;
    }

    public ListNode reverseKGroup(ListNode head, int k) {
        Result result = takeFirstK(head, k);
        if (result.preLen < k) {
            return result.preList;
        } else {
            ListNode reversed = reverse(result.preList);
            return concat(reversed, reverseKGroup(result.nextList, k));
        }
    }

    public static void main(String[] args) {
        ListNode l1 = new ListNode(1);
        ListNode l2 = new ListNode(2);
        ListNode l3 = new ListNode(3);
        ListNode l4 = new ListNode(4);
        ListNode l5 = new ListNode(5);
        l1.next = l2;
        l2.next = l3;
        l3.next = l4;
        l4.next = l5;
        Solution s = new Solution();
        ListNode l = s.reverseKGroup(l1, 2);
        assert l.val == 2;
    }
}