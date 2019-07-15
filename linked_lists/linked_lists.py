class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None
class Linked_List:
    def __init__(self,head=None):
        if head:
            head=Node(head)
            self.head=head
        else:
            self.head=head
    def append(self,value):
        """ Append a node to the end of the list """
        node=Node(value)
        if not(self.head):
            self.head=node
        else:
            current_node=self.head
            while current_node.next!=None:
                current_node=current_node.next
            current_node.next=node
            node.prev=current_node
        return True
    def prepend(self,value):
        """Preprends a node to head"""
        node=Node(value)
        current=self.head
        if current:
            node.next=current
            current.prev=node
            self.head=node
            return True
        else:
            self.head=node

    def get_position(self,position):
        """Get node in the giving position
           Assume the first position starts from 1
        """
        if position>0:
            counter=1
            current_node=self.head
            while current_node:
                if counter==position:
                    return current_node
                else:
                    current_node=current_node.next
                    counter+=1
            return None
        else:
            return None

    def insert(self,value,pos):
        """Inserts the given node at pos,
           if pos=3, the node gets inserted between the 2nd and 3rd node
           if pos is greater than the length of the list append to the end of the list
        """
        if pos<1:
            self.prepend(value)
            return
        node=Node(value)
        counter=1
        length=self.size()
        current_node=self.head
        if pos>=length :
            self.append(value)
            return
        if pos==1:
            node.next=current_node
            self.head=node
            return
        if pos==2:
            node.next=self.head.next
            self.head.next=node
            node.prev=self.head
            return
        while current_node and counter<pos:
            current_node=current_node.next
            counter+=1
        if current_node:
            current_node.prev.next=node
            node.prev=current_node.prev
            node.next=current_node
            current_node.prev=node
            return True
        return False
    def delete(self,value):
        """Deletes the first node with the given value"""
        current=self.head
        if self.head:
            if self.head.value==value:
                self.head=current.next
                return True
        while current:
            if current.value==value:
                break
            else:
                current=current.next
        if current:
            if current.prev:
                current.prev.next=current.next
            if current.next:
                current.next.prev=current.prev
            return True
        return False
    def to_list(self):
        """Returns a python list containing the elements of the linked list"""
        l=[]
        current=self.head
        while current:
            l.append(current.value)
            current=current.next
        return l
    def search(self,value):
        """Searches for value in the list and returns the node,returns None if not found"""
        current=self.head
        while current:
            if current.value==value:
                return current
            current=current.next
        return None
    def pop(self):
        current=self.head
        if current:
            self.head=current.next
        return current
    def size(self):
        count=1
        current=self.head
        while current:
            current=current.next
            count+=1
        return count
## Test your implementation here

# Test prepend
linked_list = Linked_List()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"

# Test append
linked_list = Linked_List()
linked_list.append(1)
print("linked_list to list should be [1]=={}".format(linked_list.to_list()))
linked_list.append(3)
print("linked_list to list should be [1,3]=={}".format(linked_list.to_list()))

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)



# Test remove
linked_list.delete(1)
print("linked_list to list should be [2 1 3 4 3]=={}".format(linked_list.to_list()))
linked_list.delete(3)
print("linked_list to list should be [2 1 4 3]=={}".format(linked_list.to_list()))
linked_list.delete(3)
print("linked_list to list should be [2 1 4]=={}".format(linked_list.to_list()))

# Test pop
value = linked_list.pop()
print("linked_list to list should be [1,4]=={}".format(linked_list.to_list()))


# Test insert
linked_list.insert(5, 1)
print("linked_list to list should be [5 1 4]=={}".format(linked_list.to_list()))
print(linked_list.insert(2, 2))
print("linked_list to list should be [5 2 1 4]=={}".format(linked_list.to_list()))
linked_list.insert(3, 6)
print("linked_list to list should be [5 2 1 4 3]=={}".format(linked_list.to_list()))

# Test size
