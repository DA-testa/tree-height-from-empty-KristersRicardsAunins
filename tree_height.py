# python3

import sys
import threading
import numpy

class Node:
    def __init__(self,index):
        self.index = index
        self.children = []
    
def compute_height(node):
    if not nodes:
        return 0
    height = []
    for node in nodes:
        heights.append(compute_height(node.children))
    return 1 + max(heights)
    
def build_tree(parents):
    nodes = [Node(i) for i in range(len(parents))]
    root = None
    for i, parent_index in enumerate(parents):
        if parent_index == -1:
            root = nodes[i]
        else:
            nodes[parent_index].children.append(nodes[i])
        return root

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    root = build_tree(parents)
    height = compute_height([root])
    print(height)
    
if __name__ = '__main__'
    main()
# print(numpy.array([1,2,3]))
