# python3

import sys
import threading
import numpy


#def compute_height(n, parents):
    # Write this function
 #   heights = [0] * n
    
    def get_height(node):
        if heights[node] != 0:
            return heights[node]
        if parents[node] == -1:
            heights[node] = 1
        else:
            heights[node] = 1 + get_height(parents[node])
        return heights[node]
    max_height = 0
    for node in range(n):
        max_height = max(max_height, get_height(node))
    # Your code here
    
    return max_height


def main():
    # implement input form keyboard and from files
    n = int(input())
    parents = list(map(int, input().split()))
    heights = [0] * n
    print(max_height)
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    
    # input values in one variable, separate with space, split these values in an array
    
    # call the function and output it's result
    
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
