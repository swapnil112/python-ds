# Python3 program to convert a binary 
# tree to its mirror 

# Utility function to create a new 
# tree node 
class newNode: 
	def __init__(self,data): 
		self.data = data 
		self.left = self.right = None

""" Change a tree so that the roles of the 
	left and right pointers are swapped at 
	every node. 

So the tree... 
		4 
		/ \ 
	2 5 
	/ \ 
	1 3 

is changed to... 
	4 
	/ \ 
	5 2 
	/ \ 
	3 1 
"""
def mirror(node): 

	if (node == None): 
		return
	else: 

		temp = node 
		
		""" do the subtrees """
		mirror(node.left) 
		mirror(node.right) 

		""" swap the pointers in this node """
		temp = node.left 
		node.left = node.right 
		node.right = temp 

""" Helper function to print Inorder traversal."""
def inOrder(node) : 

	if (node == None): 
		return
		
	inOrder(node.left) 
	print(node.data, end = " ") 
	inOrder(node.right) 

# Driver code 
if __name__ =="__main__": 

	root = newNode(1) 
	root.left = newNode(2) 
	root.right = newNode(3) 
	root.left.left = newNode(4) 
	root.left.right = newNode(5) 

	""" Print inorder traversal of 
		the input tree """
	print("Inorder traversal of the", 
			"constructed tree is") 
	inOrder(root) 
	
	""" Convert tree to its mirror """
	mirror(root) 

	""" Print inorder traversal of 
		the mirror tree """
	print("\nInorder traversal of", 
			"the mirror treeis ") 
	inOrder(root) 

# This code is contributed by 
# Shubham Singh(SHUBHAMSINGH10) 
