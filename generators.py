lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]
def my_enumerate(iterable,start=0):
    index=0
    while index<len(iterable):
        yield start,iterable[index]
        start+=1
        index+=1
def chunker(iterable, size):
    """Yield successive chunks from iterable of length size."""
    start=0
    end=size
    while end<len(iterable):
        yield iterable[start:end]
        start+=size
        end+=size
    if end>=len(iterable):
        yield iterable[start:]

for chunk in chunker(range(25), 4):
    print(list(chunk))
for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))
