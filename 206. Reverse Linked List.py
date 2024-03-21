class Solution(object):
    def reverseList(self, head):
        if not head:
            return None
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
