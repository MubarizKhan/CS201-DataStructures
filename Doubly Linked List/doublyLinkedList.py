##
##  Doubly linked List in Python Mubariz Khan P180010
##


class Node(object):

    def __init__(self, val, prev, nex):
        self.val = val
        self.prev = prev
        self.next = nex


class Dll(object):

    def __init__(self):
        self.head = None

    
    def append(self,x):
    
        if self.head == None:
            self.head = Node(x,None, None)
            
            print ("Added to Head")

        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
        
            temp = Node(x,cur,None)
            cur.next = temp
            print ("Added")
            


    def print(self):
        # listt = []
        cur = self.head
        # self.head.prev = cur

        while cur.next != None:
            
            # print (cur.val, "This is the previous val")
            print (cur.val)
            cur = cur.next
            
        
        while cur != None:
            print(cur.val)
            cur = cur.prev
            


var = Dll()
var.append(222)
var.append(234)
var.append(345)

var.print()

