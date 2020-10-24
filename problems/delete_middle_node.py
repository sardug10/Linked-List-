# Delete a node in the middle of the linked lost i.e, any node except first and the last

from list import Singly_linked_list

def remove(value):
    list = Singly_linked_list()
    list.push('a')
    list.push('b')
    list.push('c')
    list.push('d')
    list.push('e')
    list.push('f')

    current = list.head
    prev = None
    for i in range(list.length):
        if current.val == value:
            prev.next = current.next

        prev = current
        current = current.next

    list.print_list()

remove('c')
