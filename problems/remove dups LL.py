# Given a sorted linked list, delete all duplicates such that each element appear only once.

# Example 1:

# Input: 1->1->2
# Output: 1->2


from list import Singly_linked_list

def duplicatesRemoval():
    linked_list = Singly_linked_list()
    linked_list.push(1)  #
    linked_list.push(1)  #
    linked_list.push(2)  #
    linked_list.push(3)  # slow
    linked_list.push(3)  #

    node_list = {}

    current = linked_list.head
    prev = None
    count = 0
    while current is not None:
        if current.val not in node_list.values():
            count += 1
            node_list[count] = current.val
            prev = current
            current = current.next

        else:
            temp = current.next
            prev.next = current.next
            current = temp

    print(node_list)
    linked_list.print_list()

duplicatesRemoval()