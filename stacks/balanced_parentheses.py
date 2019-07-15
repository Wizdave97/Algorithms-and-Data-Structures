from stacks import Stack
import re

def parentheses_checker(string):
    opening_stack=Stack()
    closing_stack=Stack()
    opening_curly_braces=Stack()
    closing_curly_braces=Stack()
    for char in string:
        if re.match(r'\(',char):
            opening_stack.push(char)
        elif re.match(r'\)',char):
            closing_stack.push(char)
        elif re.match(r'\{',char):
            opening_curly_braces.push(char)
        elif re.match(r'\}',char):
            closing_curly_braces.push(char)
    if opening_stack.size()==closing_stack.size() and opening_curly_braces.size()==closing_curly_braces.size():
        return True
    return False
a = parentheses_checker('((3^2 + 8)*(5/2))/(2+6)')
print(a)
print ("Pass" if a else "Fail")
b = parentheses_checker('((3^2 + 8)*(5/2))/(2+6))')
print(b)
print ("Pass" if not b else "Fail")
