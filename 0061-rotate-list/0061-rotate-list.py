# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        if not head or k == 0:
            return head

        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        k = k % length
        if k == 0:
            return head

        tail.next = head  # Make it circular
        steps_to_new_head = length - k
        new_tail = tail
        while steps_to_new_head:
            new_tail = new_tail.next
            steps_to_new_head -= 1

        new_head = new_tail.next
        new_tail.next = None
        return new_head