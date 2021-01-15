def reverseList(self, head):
            next=None
            while head:
                head.next,head,next=next,head.next,head
            return next
