#!/usr/bin/python3
class Node:
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None

def lca(root,a,b):
    if root is None:
        return -1;
    if(root.val == a or root.val == b):
        return root.val

    x = lca(root.left,a,b)
    y = lca(root.right,a,b)
    if (x != -1 and y != -1):
        return root.val
    return (x if x!=-1 else y)

def createTree():
    a = input("Enter root value");
    q = []
    root = Node(a)
    print(root.left,root.right,root.val)
    q.insert(0,root)
    print("enter -1 if node not present")
    while q:
        cur = q.pop()
        l = input(f"Enter the left of {cur.val} ")
        r = input(f"Enter the right of {cur.val} ")

        if l!= "-1":
            cur.left = Node(l)
            q.insert(0,cur.left)
        if r!= "-1":
            cur.right = Node(r)
            q.insert(0,cur.right)
    return root


    
def main():
   root = createTree() 
   a,b=input("Enter Start and End vertices ").split()
   print(lca(root,a,b))

if __name__ == "__main__":
    main()
