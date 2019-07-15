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
def even_after_odd(l_list):
    """
       This function takes a linkedlist of integer values and rearranges it such that all
       even numbers come after all odd numbers in the same relative order of the original list
       Args:
        arg1: linked list with integer node values
    """
    current=l_list.head
    if current is None:
        return
    while current.next:
        if (current.value%2==0) and (current.next.value%2!=0):
            current_value=current.value
            next_value=current.next.value
            current.value=next_value
            current.next.value=current_value
            current=l_list.head
        current=current.next
    return l_list
"""
Time complexity for even_after_odd algorithm
the loop resets back to the head after every rearrangement so the in the worst case scenario there exists an
even interger after every odd integer
If k is a constant that depends on the degree of sorting the number of odd numbers in the  list
f(n)=kn
O(f(n))=>O(n)
"""
arr = [1, 2, 3, 4, 5, 6,9,8,11,12,14,16,17]
solution = [1, 3, 5,9,11,17, 2, 4, 6,8,12,14,16]
l_list=LinkedList()
for i in arr:
    l_list.append(i)
print(list(l_list))
even_after_odd(l_list)
print(list(l_list))
print('Pass' if list(l_list)==solution else "Fail")
