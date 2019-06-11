"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('calls.csv','r') as calls_list:
    calls_list_csv=csv.reader(calls_list)
    call_list=list(calls_list_csv)
    last_call=call_list[-1]
with open('texts.csv','r') as texts_list:
    texts_list_csv=csv.reader(texts_list)
    text_list=list(texts_list_csv)
    first_text=text_list[0]
"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
print("First record of texts, {} texts {} at time {}".format(*first_text))
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(*last_call))
