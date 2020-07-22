## This Data Struture is very efficient in terms of searching as it minimize half its space complexity each time it iterate. ##
## This mean its big O complexity is O(logn)   ##

class BinarySearchTree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addChild(self, data):
        if data == self.data:
            # if data is a duplicate then return
            return 

        if data < self.data:
            # add data in the left node
            if self.left:
                self.left.addChild(data)
            else:
                self.left = BinarySearchTree(data)
        
        else: 
            # add data in the right node
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BinarySearchTree(data)

    def in_order_traversal(self):
        elements = []

        # visit left node
        if self.left:
            elements += self.left.in_order_traversal()

        # visit root node
        elements.append(self.data)
        
        # visit right node
        if self.right:
            elements += self.right.in_order_traversal()
        return elements


    def search(self, value):
        if self.data == value:
            return True
        
        if value < self.data:
            ## Searching in left node
            if self.left:
                return self.left.search(value)
            else:
                return False

        if value > self.data:
            ## Searching in right node
            if self.right:
               return self.right.search(value)
            else:
                return False

    def getMax(self):
        if self.right is None:
            return self.data
        return self.right.getMax()

    def getMin(self):    
        if self.left is None:
            return self.data
        return self.left.getMin()

    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)

        else:
            if self.right is None and self.left is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            min_val_right_tr3 = self.right.getMin()
            self.data = min_val_right_tr3
            self.right = self.right.delete(min_val_right_tr3) 
        
        return self







def buildTree(arr):
    root = BinarySearchTree(arr[0])

    for i in range(1, len(arr)):
        root.addChild(arr[i])

    return root


if __name__ == "__main__":
    arr = [4,6,1,2,5,15,7,9,20,10,8,3]
    tree = buildTree(arr)
    tree.delete(5)
    print(tree.in_order_traversal())

