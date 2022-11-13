#==============================================================================
#    CS233T – Unit 4 -Submission Node – Question 2
#    Filename: CS233T-2003C-01_Unit3_Question1_Gilchrist_Grant
#    Author: Grant Gilchrist
#    Problem: 
#==============================================================================


#       TREE STRUCTURE:
#            (0100)
#            /    \
#      (0060)      (0110)
#      /   \        /   \
#   (0050) (0067) (0109) (0111)


#----------------------------------------------------------
# Tree structure adds nodes based on if the data is less than or greater than the node and sorts it left or right of previous nodes respectively.

class Groot:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def add(self,data):
        if data < self.data:
            if self.left is None:
                self.left = Groot(data)
            else:
                self.left.add(data)
        elif data > self.data:
            if self.right is None:
                self.right = Groot(data)
            else:
                self.right.add(data)

                        
#----------------------------------------------------------                    
# to print in-order the print statement is in the middle, this causes all the nodes to print all the left side then all the right side

    def PrintInOrder(self):
        if self.left:
            self.left.PrintInOrder()
        print(self.data)
        if self.right:
            self.right.PrintInOrder()

# to print pre-order the print statement is in the beginning, this causes all the nodes to be printed out like a Depth First Search
    def PrintPreOrder(self):
        print(self.data)
        if self.left:
            self.left.PrintPreOrder()
        if self.right:
            self.right.PrintPreOrder()
            
# to print post-order the print statement is at the end, this causes the nodes to print at the deepest most branches and work backwards starting on the left side until it ends at the root node. 
    def PrintPostOrder(self):
        if self.left:
            self.left.PrintPostOrder()
        if self.right:
            self.right.PrintPostOrder()
        print(self.data)
            
            
#---------------------------------------------------------- 

G = Groot('0100')
G.add('0060')
G.add('0050')
G.add('0067')
G.add('0110')
G.add('0109')
G.add('0111')


print('\n''Binary Tree In-Order Traversal:')
G.PrintInOrder()
print('\n''Binary Tree Pre-Order Traversal:')
G.PrintPreOrder()
print('\n''Binary Tree Post-Order Traversal:')
G.PrintPostOrder()