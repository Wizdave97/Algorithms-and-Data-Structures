from stack_with_llist import Stack
import re

def minimum_bracket_reversals(string):
    """"Returns minimum number of reversals for the curly braces to be balanced
        INPUT
        arg: string of curly braces in the form '{{{}}'
        Return: integer indicating the number of reversals for curly braces to be balanced or -1 if it cant be balanced
    """
    if len(string)%2==1:
        return -1
    stack=Stack()
    for bracket in string:
        if not stack.is_empty():
            top=stack.top()
            if top!=bracket:
                if top=='{' and bracket=='}':
                    stack.pop()
                    continue
                else:
                    stack.push(bracket)
            else:
                stack.push(bracket)
        else:
            stack.push(bracket)
    count=0
    while not stack.is_empty():
        first=stack.pop()
        second=stack.pop()
        if first=='{' and second=='{':
            count+=1
        elif first=='{' and second=='}':
            count+=2
        elif first=='}' and second=='}':
            count+=1
        elif second==None and first:
            return -1
    return count

def test_function(test_case):
    input_string = test_case[0]
    expected_output = test_case[1]
    output = minimum_bracket_reversals(input_string)
    print(output)
    if output == expected_output:
        print("Pass")
    else:
        print("Fail")
test_case_1 = ["}}}}", 2]
test_function(test_case_1)
test_case_2 = ["}}{{", 2]
test_function(test_case_2)
test_case_3 = ["{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}", 13]
test_function(test_case_3)
test_case_4= ["}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{", 2]
test_function(test_case_4)

test_case_5 = ["}}{}{}{}{}{}{}{}{}{}{}{}{}{}{}", 1]
test_function(test_case_5)
test_case_6 = ["'{{{}}'", -1]
test_function(test_case_6)
