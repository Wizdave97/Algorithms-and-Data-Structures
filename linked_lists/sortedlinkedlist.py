
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)
class SortedLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """
        Append a value to the Linked List in ascending sorted order

        Args:
           value(int): Value to add to Linked List
        """
        # TODO: Write your sorted append function here
        node=Node(value)
        if self.head is None:
            self.head=node
            return
        elif self.head:
            if self.head.value>=value:
                node.next=self.head
                self.head=node
                return
        current=self.head
        while current.next:
            if current.next.value>=value:
                node.next=current.next
                current.next=node
                return
            current=current.next
        current.next=node
    def __iter__(self):
        current=self.head
        while current:
            yield current.value
            current=current.next
"""
Calculating the time complexity of the append algorithm
Since the elements must always be added in ascending the order, meaning that any given time the list is always sorted,
adding random integer that is larger than all the elements currently in the list will lead to the loop running for the n times
where n is the number of nodes in the loop at any given time, therefore for the worst case scenario, the time complexity can be approximated as
O(n)
"""
linked_list = SortedLinkedList()
linked_list.append(3)
print ("Pass" if (linked_list.head.value == 3) else "Fail")
linked_list.append(2)
print ("Pass" if (linked_list.head.value == 2) else "Fail")
linked_list.append(6)
node = linked_list.head.next.next
print ("Pass" if (node.value == 6) else "Fail")
linked_list.append(4)
linked_list.append(3)
print(list(linked_list))

def sort(array):
    """
    Given an array of integers, use SortedLinkedList to sort them and return a sorted array.

    Args:
       array(array): Array of integers to be sorted
    Returns:
       array: Return sorted array
    """
    l_list=SortedLinkedList()
    for val in array:
        l_list.append(val)
    return list(l_list)
"""
Time complexity for the sort algorithm
let the length of the input array be N,
The for loop runs N times
for each iteration in the for loop, the append function also runs for the current length of the list.
Assume for the worst case the length of the list is N,
The conversion of the list back to an array also takes N times approximately
then,
f(n)=N*N + N + 1
f(n)=N^2 + N + 1
f(n)=N^2 + N
Aproximating for higher order terms, we have,
O(N^2) which is a quadratic complexity in the worst case,
This sorting algorithm is the equivalent to insertion sort algorithm, but slower than quicksort and mergesort with O(NlogN)
"""
print ("Pass" if (sort([4, 8, 2, 1, -3, 1, 5]) == [-3, 1, 1, 2, 4, 5, 8]) else "Fail")
