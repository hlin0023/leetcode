class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                while slow is not head:
                    slow = slow.next
                    head = head.next
                return slow
        return None

if __name__ == "__main__":
    head = [3,2,0,-4], pos = 1
    print(detectCycle(head))