# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
Explanation: 342 + 465 = 807.

from list import Singly_linked_list

def list_sum():
    # initializing first list
    first_list = Singly_linked_list()
    first_list.push(1)
    first_list.push(2)
    first_list.push(3)
    # first_list.push(4)

    # initializing second list
    second_list = Singly_linked_list()
    second_list.push(5)
    second_list.push(6)
    second_list.push(7)
    # second_list.push(8)

    #initializing the result list
    result = Singly_linked_list()

    # handling the code if the length of 2 lists are different
    if first_list.length < second_list.length:
        for i in range(0, second_list.length - first_list.length):
            first_list.push(0)
    elif first_list.length > second_list.length:
        for i in range(0, first_list.length - second_list.length):
            second_list.push(0)
    else:
        pass


    first_digit = first_list.head    # 5
    second_digit = second_list.head  # 7
    carry = 0 # forwarding this to the next node
    for i in range(0,first_list.length):
        temp = first_digit.val + second_digit.val + carry   # 5 + 7 + 0 = 12
        # print(temp)
        temp_array = [int(i) for i in str(temp)]            # [1, 2]
        if len(temp_array) is 1:
            carry = 0
            result.push(temp_array[0])
        else:
            carry = temp_array[0]                           # carry = 1
            if(i is first_list.length-1):
                result.push(temp_array[1])
                result.push(temp_array[0])
            else:
                result.push(temp_array[1])                  # result = 2

        first_digit = first_digit.next
        second_digit = second_digit.next

    result.print_list()


list_sum()