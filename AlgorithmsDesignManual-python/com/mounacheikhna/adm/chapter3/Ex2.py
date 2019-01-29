"""
class ListNode(object):
    def __init__(self, x, nxt=None):
        self.val = x
        self.next = nxt

    def str(self):
        return 'ListNode{' + 'val=' + str(self.val) + ', ' + (self.next.str() if self.next else '') + '}'
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def str(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, value):
        if not self.head:
            self.__initialize_list(value)
        else:
            node = Node(value)
            self.tail.next = node
            self.tail = node

    def print_list(self):
        current_node = self.head

        print('head ->', end=' '),
        while current_node is not None:
            print(current_node.value.str(), ' -> ', end=' '),

            current_node = current_node.next

        print('tail')

    def reverse(self):
        p = head = self.head

        while p:
            temp = p
            p = head.next
            t_next = p.next
            head.next = t_next
            p.next = temp

            if not head.next:
                self.head = p
                break

    def __initialize_list(self, value):
        self.head = Node(value)
        self.tail = self.head


ll = LinkedList()
ll.add_node(Node(1))
ll.add_node(Node(2))
ll.add_node(Node(3))
ll.print_list()
ll.reverse()
ll.print_list()

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
