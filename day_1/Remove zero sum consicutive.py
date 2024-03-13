class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head):
        prefix_sum = 0
        hashmap = {}
        
        dummy = ListNode(0)
        dummy.next = head
        hashmap[0] = dummy
        
        while head:
            prefix_sum += head.val
            
            if prefix_sum in hashmap:
                p = hashmap[prefix_sum]
                start = p
                p_sum = prefix_sum
                
                while start != head:
                    start = start.next
                    p_sum += start.val
                    if start != head:
                        hashmap.pop(p_sum)
                
                p.next = start.next
                
            else:
                hashmap[prefix_sum] = head
            
            head = head.next
        
        return dummy.next
