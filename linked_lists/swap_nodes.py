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
def create_linked_list(arr):
    if len(arr)==0:
        return None
    l_list=LinkedList()
    for data in arr:
        l_list.append(data)
    return l_list
def swap_nodes(head,left_index,right_index):
    """
    :param: head- head of input linked list
    :param: left_index - indicates position
    :param: right_index - indicates position
    return: head of updated linked list with nodes swapped
    TODO: complete this function and swap nodes present at left_index and right_index
    Do not create a new linked list
    """
    current=head
    count=0
    left_node=None
    right_node=None
    before_left=None
    before_right=None
    if left_index>right_index or left_index==right_index:
        return head
    while current:
        if count==left_index:
            left_node=current
        if (left_index-count) == 1:
            before_left=current
        if (right_index-count) == 1:
            before_right=current
        if count==right_index:
            right_node=current
            break
        count+=1
        current=current.next
    if before_left is None:
        head=right_node
    else:
        before_left.next=right_node
    before_right.next=left_node
    temp=left_node.next
    left_node.next=right_node.next
    right_node.next=temp
    return head
arr = [3, 4, 5, 2, 6, 1, 9]
solution =[3, 4, 5, 6, 2, 1, 9]
l_list= create_linked_list(arr)
left_index = 3
right_index = 4
updated_head=swap_nodes(l_list.head,left_index,right_index)
print("Pass" if list(l_list)==solution else "Fail")
l_list.head=updated_head
print(list(l_list))
