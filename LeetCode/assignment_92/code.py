

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    if not head or left == right:
        return head  # Không cần đảo nếu danh sách rỗng hoặc left == right

    dummy = ListNode(0)  # Tạo node giả để xử lý dễ hơn khi left = 1
    dummy.next = head
    prev = dummy

    # Bước 1: Di chuyển đến node trước vị trí `left`
    for _ in range(left - 1):
        prev = prev.next

    # Bước 2: Bắt đầu đảo ngược đoạn từ left -> right
    curr = prev.next
    next_node = None
    for _ in range(right - left):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp  # Cập nhật node đầu của đoạn bị đảo
    return dummy.next
