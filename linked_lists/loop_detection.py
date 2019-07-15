class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return
list_with_loop = LinkedList([2, -1, 3, 0, 5])

# Creating a loop where the last node points back to the second node
loop_start = list_with_loop.head.next

node = list_with_loop.head
while node.next:
    node = node.next
node.next = loop_start

def is_circular(l_list):
    """"Returns true if the list is circular and false otherwise
        Args: linked list
    """
    slow_runner=l_list.head
    fast_runner=l_list.head
    while slow_runner and fast_runner:
        print(slow_runner.value,fast_runner.value)
        if fast_runner.next:
            fast_runner=fast_runner.next.next
        else:
            fast_runner=fast_runner.next
        slow_runner=slow_runner.next
        if fast_runner and slow_runner:
            if slow_runner.value==fast_runner.value:
                return True
    return False
print(is_circular(list_with_loop))
