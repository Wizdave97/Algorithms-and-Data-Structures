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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
def possible_telemarketers(calls,texts):
    phonebook={}
    texting_list={}
    receiving={}
    for record in texts:
        texting_list[record[0]]=record[0]
        texting_list[record[1]]=record[1]
    for record in calls:
        receiving[record[1]]=record[1]
    for record in calls:
        if not(texting_list.get(record[0])) and not(receiving.get(record[0])):
            phonebook[record[0]]=record[0]
    phonebook=list(phonebook.values())
    for i,tel in enumerate(phonebook):
        phonebook[i]+='\n'
    phonebook=sorted(phonebook)
    phonebook=''.join(phonebook)
    print("These numbers could be telemarketers:\n{}".format(phonebook))
possible_telemarketers(calls,texts)

"""
Time complexity can be calculated as
f(n)=7+2n+n+2n
    =5n+7
Approximated as O(n)
"""
