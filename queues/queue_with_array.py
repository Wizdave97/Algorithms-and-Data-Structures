class Queue():
    def __init__(self):
        self.items=[]
        self.num_elements=0
    def enqueue(self,element):
        self.items.insert(0,element)
        self.num_elements+=1
    def dequeue(self):
        if self.num_elements!=0:
            top=self.items[-1]
            self.items[-1:]=[]
            self.num_elements-=1
            return top
        return None
    def front(self):
        if self.num_elements!=0:
            return self.items[-1]
        return None
    def is_empty(self):
        if self.num_elements==0:
            return True
        return False
    def size(self):
        return self.num_elements
    def __iter__(self):
        for i in range(-1,-(len(self.items)+1),-1):
            yield self.items[i]
# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(list(q))
# Test size
print ("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print(list(q))
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail")
