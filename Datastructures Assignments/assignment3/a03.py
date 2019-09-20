class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, index, val):
        new_node = Node(val)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        temp = self.head

        counter = 0

        while temp is not None and counter < index:
            prev = temp
            temp = temp.next
            counter += 1

        prev.next = new_node
        new_node.next = temp

    def push(self,val):
        if self.head is None:
            self.head = Node(val)
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        
        temp.next = Node(val)

    def pop(self):
        
        if self.head is None:
            raise Exception("This doesn't work")

        if self.head.next is None:
            self.head.next = None
            return
        temp = self.head
        while temp.next is not None:
            prev = temp
            temp = temp.next

        val = temp.val
        prev.next = None
        return val


    def len(self):
        counter = 0
        temp = self.head

        # if temp is None:
        #     return counter
       
        while temp != None:
            temp = temp.next
            counter += 1
        
        # print (total)
        return counter

    def get(self,index):
        
    
        temp = self.head
        counter = 0

        length = self.len()

        
        while counter != length-1:
            if counter == index:
                return temp.val
            
            counter += 1
            prev = temp
            temp = temp.next

        if index > counter:
            raise IndexError("Out of bound")

        if temp is None:
            raise Exception("Index error")

        return temp.val

    def __str__(self):
        temp = self.head
        msg = "["
        while temp is not None:
            msg += str(temp.val) + ", "
            temp = temp.next

        msg = msg.rstrip(", ")
        msg += "]"
        return msg

    
    def remove(self, val):
        temp = self.head  
        # counter = 0
        # if index == counter:
        #     self.head.next = temp.next
        if temp is None:
            raise Exception("Head is empty")
        
        if temp is not None: #to check if head is the same as val
            if temp.val == val:
                print("found")
                self.head = temp.next
                return 

        while temp is not None:
            if temp.val == val:
                break

            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
    
   
    


if __name__ == "__main__": 
    l = LinkedList() 
    l.push(5) 
    l.push(6) 

    print(l)

    # l.get(2)

    print(l.len(), ": Length")

    # l.pop() 
    # print(l.len())

    #l.remove(5)
    l.insert(3, 19)
    print(l)
    

    print( "getting ", l.get(3)) # Should say "IndexError: Index out of bound"

    # m = LinkedList()
    # m.push(23)
    # m.push(345)
    # m.push(34)

    # m.remove(23)
    # print(m)
