# python3

import sys
import threading
import numpy
import os
    
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
      
def find_height(n, parent):
    nodes = [Node(i) for i in range (n)]
    root = None
        
    for i in range(n):
        if parent[i] == -1:
            root = nodes[i]
        else:
            parent_node = nodes[parent[i]]
            parent_node.children.append(nodes[i])
                
    max_height = 0
    queue = [(root, 1)]
    
    while queue:
        node, level = queue.pop(0)
        if level > max_height:
            max_height = level
        for child in node.children:
            queue.append((child, level + 1))
    return max_height

def main():
    while True:
        vai = input().strip().upper()
        if vai == "I":
            input_string = input()
            n = int(input_string.split()[0])
            parent = list(map(int, input_string.split()[1:]))
            break
        elif vai == "F":
            fails = input()
            if os.path.exists(fails):
                with open(fails) as f:
                    input_string = f.readline().strip()
                    n = int(input_string.split()[0])
                    parent = list(map(int, input_string.split()[1:]))
                break
            
    height = find_height(n, parent)
    print(height)
    pass

if __name__ == '__main__':
    sys.setrecursionlimit(10**7)
    threading.stack_size(2**27)
    threading.Thread(target=main).start()
