# Node:- Val and the pointer Next pointing to the next node in the list
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Singly_linked_list:
    def __init__(self):
        # every linked list should have a head,tail and length
        self.head = None
        self.tail=None
        self.length = 0

    def push(self,val): # Insert an element at the end
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self): # remove the last element from the list
        if self.length == 0:
            return 'LIST IS EMPTY'


        node = self.head
        new_tail = node
        while node.next is not None:
            new_tail = node
            node = node.next
        self.tail = new_tail
        self.tail.next = None
        self.length -= 1

        return node.val

    def shift(self): # remove the 1st element in the list
        prev_head = self.head
        self.head = prev_head.next
        self.length -= 1

        return prev_head.val

    def unshift(self,val): #inserts the element at the starting
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def get(self,index): # get the element at the particular position
        if index > self.length or index < 0:
            return None
        node=self.head
        for i in range(1,index):
            node=node.next

        return node.val

    def set(self,index,new_val): # set the value of a node at a particular position to a new val
        if index > self.length or index < 0:
            return None
        node = self.head
        for i in range(1, index):
            node = node.next

        node.val = new_val
        return node.val

    def insert(self,position,val): # inserts a new node at the given position
        new_node = Node(val)
        if position == 1:
            self.unshift(val)
        elif position == self.length:
            self.push(val)
        else:
            prev_node = self.head
            for i in range(1,position-1):
                prev_node = prev_node.next

            new_node.next = prev_node.next
            prev_node.next = new_node
            self.length += 1

    def remove(self,position): # removes a node from the given position

            if position > self.length or position < 0:
                return None
            if position == 1:
                self.shift()
            elif position == self.length:
                self.pop()
            else:
                current_node = self.head  # node that we want to remove
                prev_node = current_node  # node previous to the current

                for i in range(1, position):
                    prev_node = current_node
                    current_node = current_node.next
            prev_node.next = current_node.next

    def reverse(self):
        prev = None
        current = self.head
        self.head=self.tail
        self.tail=current
        for i in range(self.length):
            next=current.next
            current.next = prev
            prev=current
            current=next

        # return self

    def begin(self): # returns the value of the HEAD node
        return self.head.val

    def end(self): # returns the value of the TAIL node
        return self.tail.val



    def print_list(self):
        node = self.head
        while node is not None:
            print(node.val)
            node = node.next


sll_1 = Singly_linked_list()
sll_1.push('Monday')
sll_1.push('Tuesday')
sll_1.push('Wednesday')
sll_1.push('Thursday')
sll_1.push('Friday')
sll_1.push('Saturday')
sll_1.push('Sunday')
# sll_1.print_list()












