class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head):
    if not head:
        print("List is empty.")
        return
    current = head
    while current:
        print(current.data, end=" -> " if current.next else " -> NULL\n")
        current = current.next

def create_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head

def split_odd_even(head):
    odd_head = odd_tail = None
    even_head = even_tail = None

    current = head
    while current:
        if current.data % 2 != 0:  # odd
            if not odd_head:
                odd_head = odd_tail = Node(current.data)
            else:
                odd_tail.next = Node(current.data)
                odd_tail = odd_tail.next
        else:  # even
            if not even_head:
                even_head = even_tail = Node(current.data)
            else:
                even_tail.next = Node(current.data)
                even_tail = even_tail.next
        current = current.next

    return odd_head, even_head

n = int(input())
arr = list(map(int, input().split()))

head = create_linked_list(arr)
print_list(head)

odd_list, even_list = split_odd_even(head)
print_list(odd_list)
print_list(even_list)
