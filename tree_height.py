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
            n = int(input())
            parent = list(map(int, input().split()))
            height = find_height(n, parent)
            print(height)
            break
        elif vai == "F":
            fails = input()
            if os.path.exists(fails):
                with open(fails) as f:
                    n = int(f.readline().strip())
                    parent = list(map(int, f.readline().strip().split()))
                    height = find_height(n, parent)
                    print(height)
                break
            else:
                print()
        else:
            print()
    #input_type = input()
    #if input_type == "I":
      #  n = int(input())
      #  parent = list(map(int, input().split()))
      #  height = find_height(n, parent)
      #  print(height)
       
    #elif input_type == "F":
        #file_name = input()
        #while 'a' in file_name:
           # print("File name cannot contain 'a'")
           # file_name = input()
       # file_path = "./tree-height-from-empty-KristersRicardsAunins/test/" + file_name
        
        #with open(file_path) as f:
           # n = int(f.readline().strip())
           # parent = list(map(int, f.readline().strip().split()))
           # height = find_height(n, parent)
          #  print(height)
           
    pass

if __name__ == '__main__':
    sys.setrecursionlimit(10**7)
    threading.stack_size(2**27)
    threading.Thread(target=main).start()
