class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def preppend(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = Node(value)
        node.next = self.head
        self.head = node
        return

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])
def reverse_linked_list(l_list):
    temp_list=LinkedList()
    for value in l_list:
        temp_list.preppend(value)
    return temp_list

l_list = LinkedList()
for value in [4,2,5,1,-3,0]:
    l_list.append(value)

print(list(l_list))
print(reverse_linked_list(l_list))
print(list(l_list) == list(reverse_linked_list(l_list)))
print ("Pass" if (list(l_list) != list(reverse_linked_list(l_list))) else "Fail")
