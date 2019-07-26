/// Runtime: 64 ms, faster than 96.66% of Swift online submissions for Add Two Numbers.
// Definition for singly-linked list.
public class ListNode {
    public var val: Int
    public var next: ListNode?
    
    public init(_ val: Int) {
        self.val = val
        self.next = nil
    }
}

class Solution {
    func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        var head, tail:ListNode?
        var head1 = l1
        var head2 = l2
        var carry = 0
        
        while (head1 != nil) || (head2 != nil) || (carry != 0) {
            let temp1, temp2:Int
            let temp = ListNode(0)
            switch head1 {
                case nil:
                    temp1 = 0
                default:
                    temp1 = head1!.val
                    head1 = head1!.next
            }
            switch head2 {
                case nil:
                    temp2 = 0
                default:
                    temp2 = head2!.val
                    head2 = head2!.next
            }
            if temp1 + temp2 + carry > 9 {
                temp.val = temp1 + temp2 + carry - 10
                carry = 1
            } else {
                temp.val = temp1 + temp2 + carry
                carry = 0
            }
            
            if head == nil {
                head = temp
                tail = head
            }else {
                tail!.next = temp
                tail = temp
            }
        }
        
        return head
    }
}

var tc1:ListNode?
tc1 = ListNode(2)

var tc2:ListNode?
tc2 = ListNode(5)

var test = Solution()

var res = test.addTwoNumbers(tc1, tc2)

while res != nil {
    print(res!.val)
    res = res!.next
}
