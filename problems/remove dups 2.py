# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

# Return the linked list sorted as well.

# Example 1:

# Input: 1->2->3->3->4->4->5
# Output: 1->2->5


from list import Singly_linked_list

def duplicatesRemoval():
    linked_list = Singly_linked_list()
    linked_list.push(1)
    linked_list.push(1)
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)

    node_list = {}

    current = linked_list.head
    count = 1

    while current is not None:
        if current.val not in node_list.keys():
            node_list[current.val] = count
            current = current.next
        else:
            node_list[current.val] = count + 1
            current = current.next


    # iterate over the dictionary to check nodes with more than 1 occurrence
    for i in node_list.copy().values():
        prev = None
        current = linked_list.head
        temp = None
        # condition for more than 1 occurrence
        if i > 1:
            # get that node
            node = list(node_list.keys())[list(node_list.values()).index(i)]
            # print(node)

            # loop through the linked_list to delete all the existence of that node
            while current is not None:
                if current.val == node:
                    if current != linked_list.head:
                        temp = current.next
                        prev.next = current.next
                        current = temp
                    else:
                        temp = current.next
                        linked_list.head = current.next
                        current = temp
                else:
                    prev = current
                    current = current.next

            del node_list[node]

    print(node_list)
    linked_list.print_list()

duplicatesRemoval()

