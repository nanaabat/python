'''
Tree.py
@author Nana Aba Turkson
@verison 5th July, 2020

'''


# A python class that represents an individual node
# in a Binary Tree


class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data


    def print_tree(self):
        print(self.data)



#create root
root = Node(1)


#children
root.left = Node(2)
root.right = Node(3)



#children of children
root.left.left = Node(4)

root.print_tree()
root.left.print_tree()
