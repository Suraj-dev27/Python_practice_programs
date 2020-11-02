#source of this code and logic is :
#yt link : https://youtu.be/rN5PhCkauD4
        
"""              1
          2              3
      4       5            6
        7 
"""

#find maximum depth of binary tree
""" class Node:
   def __init__(self,key):
       self.data = key
       self.left = None
       self.right = None
def height_tree(a):
   if(a==None):
       return 0
   else:
       ldepth = height_tree(a.left)
       rdepth = height_tree(a.right)

       if ldepth>rdepth:
           return(1+ldepth)
       else:
           return(1+rdepth)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.right=Node(6)
root.left.left.right=Node(7)

print('height of btree:',height_tree(root)) """


#find minimum depth of binary tree
#yt link : https://youtu.be/LMi4gxO0DP4
class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None
def height_tree(root):
    if root == None:
        return 0
    else:
        ldepth = height_tree(root.left)
        rdepth = height_tree(root.right)
    if ldepth > rdepth:
        return (1+rdepth)
    else:
        return (1+ldepth)

root=Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.left.left.right = Node(7)


print(height_tree(root))
#2 is right ans 




