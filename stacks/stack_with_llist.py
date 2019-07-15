class Node():
    def __init__(self,element):
        self.data=element
        self.next=None
class Stack():
    def __init__(self):
        self.head=None
        self.num_elements=0
    def push(self,element):
        if not(self.head):
            node=Node(element)
            self.head=node
            self.num_elements+=1
        else:
            node=Node(element)
            node.next=self.head
            self.head=node
            self.num_elements+=1
            return True
    def pop(self):
        if not(self.head):
            return None
        val=self.head.data
        self.head=self.head.next
        self.num_elements-=1
        return val
    def top(self):
        if self.head:
            return self.head.data
        else:
            return None
    def size(self):
        return self.num_elements
    def is_empty(self):
        if not(self.head):
            return True
        return False
    def __iter__(self):
        current=self.head
        while current:
            yield current.data
            current=current.next
