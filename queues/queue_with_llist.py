class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
        self.num_elements=0
    def enqueue(self,element):
        node=Node(element)
        if not self.head:
            self.head=node
            self.tail=node
            self.num_elements+=1
            return element
        else:
            current=self.tail
            current.next=node
            self.tail=node
            self.num_elements+=1
            return element
    def dequeue(self):
        if self.head:
            top=self.head.data
            self.head=self.head.next
            self.num_elements-=1
            return top
        else:
            return None
    def front(self):
        if self.head:
            return self.head.data
        else:
            return None
    def size(self):
        return self.num_elements
    def __iter__(self):
        current=self.head
        while current:
            yield current.data
            current=current.next
# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print ("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail")
