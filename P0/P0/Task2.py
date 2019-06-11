"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
def longest_call(calls):
    phonebook={}
    for record in calls:
        phonebook[record[0]]=phonebook.get(record[0],0)+int(record[-1])
        phonebook[record[1]]=phonebook.get(record[1],0)+int(record[-1])
    longest_time=max(list(phonebook.values()))
    telephone=[number for number in phonebook if phonebook[number]==longest_time]
    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(*telephone,longest_time))
longest_call(calls)
"""
worst case time complexity of the algorithm
the for loop runs for all the values in the list on the worstcase
f(n)=4 + 2*n
    =2n + 4
O(f(n))= 2n + 4
time complexity can be approximated as O(n)
"""
