
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def str(self):
        return 'ListNode{' + 'val=' + str(self.value) + ', ' + (self.next.str() if self.next else '') + '}'


def reverse(head):
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev


def reverseSol2(head):
    prev = None
    while head:
        nxt, head.next = head.next, prev
        prev, head = head, nxt
    return prev


node1 = Node(1)
node1.next = Node(2)
node1.next.next = Node(3)
print(node1.str())
print(reverse(node1).str())

''''
def reverse(head):
    dummy = ListNode(0, head)  # temp
    prev, p = None, head
    while p:
        # if prev:
        #    prev.next = None
        p.next = prev
        prev = p
        p = p.next
    return dummy.next

node1 = ListNode(1, ListNode(2, ListNode(3)))
print(reverse(node1).str())
'''
