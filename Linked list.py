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



if __name__ == "__main__":
    
    L = List()
    L.append(23)
    L.append(233)
    L.append(3423)
    L.append(23345)
    L.append(46666)

    L.print()


        