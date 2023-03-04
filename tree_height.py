# python3

import sys
import threading
import numpy
    
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
            parent_node = nodes[parenti[i]]
            parent_node.children.append(nodes[i])
                
    max_height = 0
    queue = [(root, 1)]
    
    while queue:
        node, level = queue.pop(0)
        if level > max_height:
            max_height = level
        for child in node.children:
            queue.append(child, level + 1)
    return max_height

def main():
    input_type = input(""I" or "F"" )
    if input_type == "I":
        n = int(input())
        parent = list(map(int, input().split()))
        height = find_height(n, parent)
        print(height)
       
    elif input_type == "F":
        file_name = input("File name: ")
        while 'a' in file_name:
            print("File name cannot contain 'a'")
            file_name = input("file name: ")
        file_path = "./data/" + file_name
        
        while open(file_path) as f:
            n = int(f.readline().strip())
            parent = list(map(int, f.readline().strip().split()))
            height = find_height(n, parent)
            print(height)
            
    pass

if __name__ == '__main__'
    sys.setrecurionlimit(107)
    threading.stack_size(227)
    threading.Thread(target=main).start()
