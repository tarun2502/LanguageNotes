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

def split_string(source, splitlist):
    for s in splitlist[]
