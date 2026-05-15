from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            nxt = head.next      # lưu node tiếp theo
            head.next = prev     # đảo chiều liên kết
            prev = head          # di chuyển prev lên
            head = nxt           # sang node tiếp theo

        return prev