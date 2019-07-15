#Implementing a stack with an array
class Stack():
    """docstring for Stack."""

    def __init__(self):
        self.data=[]
        self.num_elements=0
    def push(self,element):
        self.data.insert(0,element)
        self.num_elements+=1
        return True
    def pop(self):
        if self.next_element<0:
            return None
        else:
            val=self.data[0]
            self.data[0]=[]
            self.num_elements-=1
            return val
    def size(self):
        return self.num_elements
    def top(self):
        if len(self.data)>0:
            return self.data[0]
        else:
            return None
    def is_empty(self):
        length=len(self.data)
        if length>0:
            return False
        else:
            return True
    def __iter__(self):
        for i in range(len(self.data)):
            yield self.data[i]
