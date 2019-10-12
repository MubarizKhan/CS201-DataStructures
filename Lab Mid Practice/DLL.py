class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            # new_node.prev = self.head
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        
        temp.next = new_node
        new_node.prev = temp

    def __str__(self):
        ret = "["
        temp = self.head
        while temp is not None:
            ret += str(temp.val) + ","
            temp = temp.next 

        ret = ret.rstrip(",")
        ret += "]"

        return ret

    def pop(self):
        if self.head is None:
            raise Exception("List is empty")
        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        prev = temp
        while temp.next is not None:
            prev = temp
            temp = temp.next
 
        tempsval = temp.val
        prev.next = None
        return tempsval
        # temp.prev = None

    def insert(self, index, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return 

        if index == 0:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            return 

        temp = self.head
        prev = temp 
        counter = 0

        while temp is not None and counter < index:
            prev = temp 
            temp = temp.next
            counter += 1


        new_node.prev = prev
        prev.next = new_node

        temp.prev = new_node
        new_node.next = temp


    def remove(self, val):
        if self.head is None:
            # self.head = None
            raise Exception("List is already empty!")

        if self.head.val == val:
            self.head = self.head.next
            self.head.prev = None
            return 

        temp = self.head
        prev = temp
        while temp is not None:
            if temp.val == val:
                gy = temp.val
                prev.next = temp.next
                temp.next.prev = prev
                return temp.val

            prev = temp
            temp = temp.next

        if temp is None:
            print("value not found")
    
    def get_last(self):
        temp = self.head
        while temp.next is not None:
            # counter += 1
            temp = temp.next

        # print (temp.val)
        return temp

    def len(self):
        temp = self.head
        counter = 0

        while temp is not None:
            counter += 1
            temp = temp.next

        # print (counter)
        return counter

    def reverse(self):
        if self.head is None:
            raise Exception("Lis is empty")

        if self.head.next is None:
            return

        new_head = self.get_last()
        processing = new_head
        temp = self.head
        temp1 = self.head

        for i in range(self.len() - 1):
            #while temp1 is not None:
            #temp = self.head
            temp = self.head
            # print("Entering while loop")
            while temp.next is not processing:
                # print("at temp with val", str(temp.val))
                temp = temp.next
            # print("Out of while")
                # print(self)
            p = processing.prev
            n = processing.next

            processing.next = temp
            temp.prev = processing          
            
            processing = temp

            # temp1 = temp1.next
        processing.next = None
        # print("gey")
        self.head.prev = None
        self.head = new_head
        return








   
        






dll = DLL()
dll.push(1)
dll.push(33)
dll.push(77)
dll.push(88)

dll.insert(0, 1111)
dll.insert(2, 9797)



print(dll)

# dll.remove(1)
# dll.remove(1111)
dll.reverse()
# dll.get_last()
# dll.len()


#print("Stuck here")
print(dll)
print("Not stucked anymore")


