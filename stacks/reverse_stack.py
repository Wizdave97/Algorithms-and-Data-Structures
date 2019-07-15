from stack_with_llist import Stack

def reverse_stack(stack):
    inverse_stack=Stack()
    for element in stack:
        inverse_stack.push(element)
    return inverse_stack
def test_function(test_case):
    stack = Stack()
    for num in test_case:
        stack.push(num)

    stack=reverse_stack(stack)
    index = 0
    while not stack.is_empty():
        popped = stack.pop()
        if popped != test_case[index]:
            print("Fail")
            return
        else:
            index += 1
    print("Pass")
test_case_1 = [1, 2, 3, 4]
test_function(test_case_1)
