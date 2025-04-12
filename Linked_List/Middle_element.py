def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

    slow=head
    fast=head

    while fast.next and fast.next.next is not None:
        slow=slow.next
        fast=fast.next.next

    if fast.next is not None:
        return slow.next
    else:
        return slow