from stack_with_llist import Stack
import re
def postfix_evaluate(exp):
    stack=Stack()
    for element in exp:
        if element=='*':
            second=stack.pop()
            first=stack.pop()
            output=first*second
            stack.push(output)
        elif element=='-':
            second=stack.pop()
            first=stack.pop()
            output=first-second
            stack.push(output)
        elif element=='/':
            second=stack.pop()
            first=stack.pop()
            output=first/second
            stack.push(int(output))
        elif element=='+':
            second=stack.pop()
            first=stack.pop()
            output=first+second
            stack.push(output)
        else:
            stack.push(int(element))
    return stack.pop()
def test_function(test_case):
    output = postfix_evaluate(test_case[0])
    print(output)
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")
test_case_1 = [["3", "1", "+", "4", "*"], 16]

test_function(test_case_1)
test_case_2 = [["4", "13", "5", "/", "+"], 6]
test_function(test_case_2)
test_case_3 = [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22]
test_function(test_case_3)
