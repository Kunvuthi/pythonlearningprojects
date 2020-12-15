

class Node:
    def __init__(self, data=None, next=None): ## Constructor of the Node 
        self.data = data
        self.next = next 


class LinkedList:
    def __init__(self):  ## Constructor of the Linked List
        self.head = None

    def insert_at_head(self, data):
        node = Node(data, self.head)  ## Making a new Node object where next pointer is pointing at the first element
        self.head = node ## Then make the node created to become the first element 

    def insert_at_tail(self,data):
        if self.head is None:
            self.head = Node(data, None) ## If there is no element in the Linked List, then create new node and automatically become first element
            return

        itr = self.head
        while itr.next:  
            itr = itr.next ## Iterating to the last element of the linked list
        
        itr.next = Node(data, None) ## Creating a new node at the next of the last element with pointer to NULL

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr =  self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' ---> '
            itr = itr.next
        print(llstr)   

    def insert_list(self, data_list):
        for data in data_list:
            self.insert_at_tail(data)

    def getLength(self):
        itr = self.head
        length = 0
        while itr:
            itr = itr.next
            length += 1
        return length

    def remove_at(self, index):
        if index < 0 or index >= self.getLength():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next

        itr = self.head
        counter = 0
        while itr:
            if counter == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            counter += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.getLength():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_head(data)
            return

        itr = self.head
        counter = 0
        while itr:
            if counter == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next    
            counter +=1 

        


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_head(5)
    ll.insert_at_head(15)
    ll.insert_list([2,15,66,76])
    ll.insert_at(2, 3)
    ll.print()