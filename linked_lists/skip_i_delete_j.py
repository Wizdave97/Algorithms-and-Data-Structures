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
def skip_i_delete_j(head,i,j):
    """
    :param: head - head of linked list
    :param: i - first `i` nodes that are to be skipped
    :param: j - next `j` nodes that are to be deleted
    return - return the updated head of the linked list
    """
    current=head
    sum=i+j-1
    count=0
    while current and current.next:
        if count>=i-1:
            print(current.next.value)
            current.next=current.next.next;
            count+=1
            if count>=sum:
                count=0
                current=current.next
                continue
            continue
        count+=1
        current=current.next
    return head

arr = arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

solution =[1, 2, 5, 6, 9, 10]

l_list=LinkedList()
for i in arr:
    l_list.append(i)
i =2
j =2
skip_i_delete_j(l_list.head,i,j)
print(list(l_list))
print("Pass" if list(l_list)==solution else "Fail")
