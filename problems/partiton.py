# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# Example:

# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5

# NOTE:- Below given solution is a naive solution, will be adding better and optimal solution for it.


from list import Singly_linked_list

def partition(num):
    list=Singly_linked_list()
    list.push(3)
    list.push(5)
    list.push(8)
    list.push(5)
    list.push(10)
    list.push(2)
    list.push(1)

    current = list.head
    partition_list = Singly_linked_list()
    for i in range(list.length):
        if(current.val < num):
            partition_list.push(current.val)
        current = current.next

    current = list.head
    for i in range(list.length):
        if(current.val >= num):
            partition_list.push(current.val)
        current = current.next

    partition_list.print_list()

partition(5)

