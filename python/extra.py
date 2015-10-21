# To meaure the run time of the program.
import time

def time_execution(code):
    start = time.clock()
    result = eval(code) #Evaluates any python code
    run_time = start - time.clock()
    return result, run_time

print time_execution('2 + 2')

def spin_loop(n):
    i = 0
    while i < n:
        i = i + 1

print time_execution('spin_loop(100000)')
#print time_execution('spin_loop(10 ** 9)')

#def split_string(source, splitlist):
#    for s in splitlist[]
    

# To convert string into number 
print ord('a') # prints 97
print ord('A') # prints 65
print chr(65) #print A
print ord(str(3)) 

# Define a function, hash_string,
# that takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.

def hash_string(keyword, bucket):
    total = 0
    for c in keyword:
        total += ord(c)
    return total%bucket

def test_hash_function(func, keys, size):
    results = [0] * size
    keys_used = []
    for w in keys:
        if w not in keys_used:
            hv = func(w, size)
            results[hv]+=1
            keys_used.append(w)
    return results

from udacity_web_crawler import  get_page
words = get_page("http://www.gutenberg.org/cache/epub/1661/pg1661.txt").split()

print test_hash_function(hash_string, words, 100)
