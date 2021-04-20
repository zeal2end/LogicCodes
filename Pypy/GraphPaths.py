#!/usr/bin/python3
from collections import defaultdict

graph = defaultdict(list) # default dict python dictornary 
def main():
    ''' takes input n: the number of vertices, e : the number of edges and then e edges to form the graph and 
    then takes int the source and destination and then print all paths in between them.'''
    a,b=int,input
    n=a(b("Enter the Number of Vertices :"))
    e = a(b("Enter the number of edges : "))
    vis = [0]*n
    def dfs(src,dest,cur = []):
        cur.append(src)
        vis[src] = 1
        if src == dest:
            print(cur);
        for a in graph[src]:
            if not vis[a]:
                dfs(a,dest);
        vis[src] = 0
        cur.pop()

    print("Enter Edges :")
    for _ in range(e):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    src,dest = map(int,input("Enter Source and Destination : ").split())

    dfs(src,dest)


if __name__ == "__main__":
    main()
