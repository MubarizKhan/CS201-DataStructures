class Node:
    def __init__(self):
        self.val = 0
        self.next = None

    def setNode(self,val,next):
        self.val = val
        self.next = next

class List:
    def __init__(self):
        self.head = None

    def append(self,val):
        if self.head == None:
            self.head = Node()
            self.head.setNode(val,None)

        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = Node()
            temp.next.setNode(val,None )
            print ("Added to list")

    def print(self):
        temp = self.head
        while temp != None:
            print (temp.val, "<----")
            temp = temp.next


    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        print (total)
        return total

    def get(self,index):
        if index>= self.length():
            print ("Index out of range: ERROR")
            return None

        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                print (cur_node.val)
                return cur_node.val
            cur_idx += 1


    def erase(self, index):
        if index >= self.length():
            print ("Index is out of range: ERROR")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                print (cur_idx,"<--- this is the value")
                return 

            cur_idx += 1

        





if __name__ == "__main__":
    
    L = List()
    L.append(23)
    L.append(233)
    L.append(3423)
    L.append(23345)
    L.append(46666)
    L.append(1234)
    L.length()
    
   
    L.erase(0)

    L.print()


        
