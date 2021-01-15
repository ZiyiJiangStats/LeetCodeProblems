
#recursive approach
class Solution(object):
    def reverseList(self, head, prev=None):
        if not head:
          return prev
  
        curr, head.next = head.next, prev
        return self.reverseList(curr, head)
