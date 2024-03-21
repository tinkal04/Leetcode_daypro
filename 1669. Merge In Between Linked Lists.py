class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        right = list1
        for i in range(b+1):
            if i == a-1:
                left=right
            if i==b+1:
                right=right.next
            right=right.next    
        temp=list2      
        while temp.next:
            temp=temp.next
        temp.next=right
        left.next=list2
        return list1




