# python3

import sys
import threading
from collections import defaultdict
    
def compute_height(n, parents):
    tree = defaultdict(list)
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]].append(i)
    
    def dfs(node):
        if not tree [node]:
            return 0
        else:
            return max(dfs(child) for child in tree[node]) + 1
    
    return dfs(root)

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))
    
main()
