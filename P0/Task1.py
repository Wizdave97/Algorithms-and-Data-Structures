"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
def count_telephone_numbers(call_list,text_list):
    phones={}
    for record in text_list:
        phones[record[0]]=phones.get(record[0],0)+1
        phones[record[1]]=phones.get(record[1],0)+1
    for record in call_list:
        phones[record[0]]=phones.get(record[0],0)+1
        phones[record[1]]=phones.get(record[1],0)+1
    total=len(phones)
    print("There are {} different telephone numbers in the records.".format(total))
count_telephone_numbers(texts,calls)

"""
Time complexity for worst case scenario is
if the combined input size for both lists is n then
f(n)=(4*n)
    =4n
O(f(n))=4n
the approximate time complexity is O(n)
"""
