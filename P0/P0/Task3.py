"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
def extract_bangalore_calls(calls):
    phonebook={}
    for record in calls:
        bangalore_match=re.match(r'\(080\)',record[0])
        area_code_match=re.match(r'\(0\d+\)',record[1])
        mobile_match=re.match(r'(7|9|8)\d{3}',record[1])
        telemarketers_match=re.match(r'(140)',record[1])
        if bangalore_match:
            if phonebook.get(record[0]):
                if area_code_match:
                    phonebook[record[0]].add(area_code_match.group(0))
                elif mobile_match:
                    phonebook[record[0]].add(mobile_match.group(0))
                elif telemarketers_match:
                    phonebook[record[0]].add(telemarketers_match.group(0))
            else:
                phonebook[record[0]]=set()
                if area_code_match:
                    phonebook[record[0]].add(area_code_match.group(0))
                elif mobile_match:
                    phonebook[record[0]].add(mobile_match.group(0))
                elif telemarketers_match:
                    phonebook[record[0]].add(telemarketers_match.group(0))
    return phonebook
def part_a(calls):
    phonebook=extract_bangalore_calls(calls)
    codes=set()
    for key in phonebook:
        codes=codes.union(phonebook[key])
    codes=sorted(list(codes))
    for i,code in enumerate(codes):
        codes[i]+='\n'
    code_string=''.join(codes)
    print("The numbers called by people in Bangalore have codes:\n{}".format(code_string))
#Part B
part_a(calls)
def part_b(calls):
    phonebook={}
    count=0
    for record in calls:
        pattern=re.compile(r'\(080\)')
        calling=pattern.match(record[0])
        if calling:
            count+=1
        recieving=pattern.match(record[1])
        if calling and recieving:
                phonebook[record[0]]=phonebook.get(record[0],0)+1
    no_calls=list(phonebook.values())
    total=0.
    for value in no_calls:
        total+=value
    percentage=round((total/count) * 100,2)
    print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage))
part_b(calls)
