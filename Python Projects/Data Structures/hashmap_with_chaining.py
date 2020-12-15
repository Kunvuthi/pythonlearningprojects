## If you don't understand, please look at the Hash Table diagram in the 'Diagrams' folder

class HashMap:
    def __init__(self):                          ## Constructor
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):    ## Converting Key into ASCII code and take the sum all of the ASCII value of char with the modulo of the size of the Hash Table 
        h = 0 
        for char in key:
            h += ord(char)
        return h % self.MAX


    def __setitem__(self, key, data): ## Adding Data inside
        h = self.get_hash(key)

        found = False
        for indx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:   ## Looking for Collision: If this has same key with the first element of the linked list, update it
                self.arr[h][indx] = (key, data)
                found = True
                break
 
        if not found:                             ## Looking for collision: if it is a new key then create new linked list with this key and data
            self.arr[h].append((key, data))

   
    def __getitem__(self, key):           ## Search through the collision chain and return the second element of the matching linked list
        h = self.get_hash(key) 
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def deleteItem(self, key):                     
        h = self.get_hash(key) 
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]

    def __delitem__(self, key):
        h = self.get_hash(key) 
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]   



if __name__ == "__main__":
    t = HashMap()
    
    t['John'] = 18
    t['John'] = 90
    t['cdd'] = 100
    
    print(t['John']) 
    print(t["cdd"])
    print(t.arr)
    
    


    