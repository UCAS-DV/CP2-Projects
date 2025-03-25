# Darius Vaiaoga, Tracing Notes

# python -m trace --trackcalls C:\Users\darius.vaiaoga\Desktop\CP2-Projects\Notes\tracing.py

import trace
import sys

tracer = trace.Trace(count=False, trace=True)

def trace_calls(frame, event, arg):

    if event == 'call':
        print(f'Calling function: {frame.f_code.co_name}')
    elif event == 'line':
        print(f'Executing line: {frame.f_lineno} in {frame.f_code.co_name}')
    elif event == 'return':
        print(f'{frame.f_code.co_name} returned {arg}')
    elif event == 'exception':
        print(f'Exception in {frame.f_code.co_name}: {arg}')

    return trace_calls

sys.settrace(trace_calls)

def sub(num_one, num_two):
    print(num_one - num_two)

def add(num_one, num_two):
    sub(num_one,num_two)
    return num_one + num_two

add(5,4)

# tracer.run('sub(5,4)')