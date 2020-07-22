## If you don't understand, please look at the Hash Table diagram in the 'Diagrams' folder

class HashMap:
    def __init__(self, size=10):                          ## Constructor
        self.MAX = size
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):    ## Converting Key into ASCII code and take the sum all with modulo of the size of the Hash Table 
        h = 0 
        for char in key:
            h += ord(char)
        return h % self.MAX


    def __setitem__(self, key, data): ## Adding Data inside
        h = self.get_hash(key)

        placed = False
        if self.arr[h]:
            if self.arr[h][0] == key:
                self.arr[h] = (key, data)
                placed = True
            else:
                for i in range(self.MAX):
                    if not (self.arr[(h + i) % self.MAX]):
                        self.arr[(h + i) % self.MAX] = (key, data)
                        placed = True
                        break                    
        
        if not self.arr[h]:
            self.arr[h] = (key, data)
            placed = True

        if not placed:
            print("Invalid Space, Hash Full")
                    
        
   
    def __getitem__(self, key):           ## Search through the collision chain and return the second element of the matching linked list
        h = self.get_hash(key) 
        for i in range(self.MAX):
            if self.arr[(h + i) % self.MAX]:
                if self.arr[(h + i) % self.MAX][0] == key:
                    return self.arr[(h + i) % self.MAX][1]

    def deleteItem(self, key):                     
        h = self.get_hash(key) 
        for i in range(self.MAX):
            if self.arr[(h + i) % self.MAX]:
                if (self.arr[(h + i) % self.MAX]) & (self.arr[(h + i) % self.MAX][0] == key):
                    self.arr[(h + i) % self.MAX] = None
                    break

    def __delitem__(self, key):
        h = self.get_hash(key) 
        for i in range(self.MAX):
            if self.arr[(h + i) % self.MAX]:
                if self.arr[(h + i) % self.MAX][0] == key:
                    self.arr[(h + i) % self.MAX] = None
                    break



if __name__ == "__main__":
    t = HashMap()
    
    t['John'] = 18
    t['John'] = 90
    t['cdd'] = 100
    
    print(t['John']) 
    print(t["cdd"])
    print(t.arr)
  
    
    


    