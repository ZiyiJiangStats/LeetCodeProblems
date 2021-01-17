class Solution:

#iterative approach 
def reverseList(self, head):
    prev = None
    while head:
        #move the head pointer to the next item 
        #curr is a temporary variable 
        # previous becomes the next 
        # current becomes the previous 
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev
