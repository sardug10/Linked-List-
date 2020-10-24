# Check if a Linked List is Palindrome

from list import Singly_linked_list

def palindrome():
    linked_list = Singly_linked_list()
    linked_list.push(1) #
    linked_list.push(2) #
    linked_list.push(3) #
    linked_list.push(4) # slow
    linked_list.push(3) #
    linked_list.push(2) #
    linked_list.push(1) # fast

    slow = linked_list.head
    fast = linked_list.head

    # LinkedList:-  1 -> 2-> 3-> 4-> 3-> 2-> 1
    # pointers:-   slow
    #              fast

    # find the middle of the linked list
    while True:
        if fast.next == None or fast.next.next == None:
            break
        else:
            slow = slow.next
            fast = fast.next.next

    # LinkedList:-  1 -> 2-> 3-> 4-> 3-> 2-> 1
    # pointers:-                slow
    #                                        fast

    # reverse the second half of the list
    prev = None
    while slow:
        next = slow.next
        slow.next = prev
        prev = slow
        slow = next

    # NOW THERE IS NO NEED OF 'SLOW' AND 'FAST' POINTERS
    # LinkedList:-  1 -> 2-> 3-> 4 <- 3 <- 2 <- 1
    # pointers:-   head                        prev


    # check palindrome
    while prev and linked_list.head:
        if prev.val != linked_list.head.val:
            return 0
        prev = prev.next
        linked_list.head = linked_list.head.next

    return 1




print(palindrome())