# Write a program to return Kth to the last node of a linked list


from list import Singly_linked_list

def kth_to_the_last(k):
    list = Singly_linked_list();
    list.push('a1')
    list.push('a2')
    list.push('a1')
    list.push('a4')
    list.push('b1')
    list.push('b2')


    position = list.length - k +1


    current = list.head
    for i in range(1,position):
        current = current.next

    return current.val



print(kth_to_the_last(3))
