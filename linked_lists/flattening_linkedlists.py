class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(value)
    def __iter__(self):
        current=self.head
        while current:
            yield current.value
            current=current.next
def merge(array):
    l_list=LinkedList()
    for i in array:
        l_list.append(i)
    return l_list
def flatten(l_list):
    store=[]
    current=l_list.head
    while current:
        if type(current.value)==LinkedList:
            for val in flatten(current.value):
                store.append(val)
        else:
            store.append(current.value)
        current=current.next
    store=sorted(store)
    store=merge(store)
    return store
"""
Time complexity of the flatten function
Assume the length of the input linkedlist is n
if all nodes are singular values then

f(n)=5 + 4*n
f(n)=5+4n
O(f(n))=n
O(n)
Assume that each node is a linked list of size M(n),
then for each iteration of the loop the for loop will run
f(n)=(5 + 4n)*M(n)*M(n)
if we assume M(n)  to be n then, dropping lower order terms
f(n)=n^3
for n numbers of nested links,
f(n)=n^n-1
O(n^n-1)
"""
linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)
third_linked_list=LinkedList(Node(8))
third_linked_list.append(linked_list)
third_linked_list.append(12)

nested_linked_list = LinkedList(Node(linked_list))
nested_linked_list.append(second_linked_list)
nested_linked_list.append(third_linked_list)
print(list(flatten(nested_linked_list)))
