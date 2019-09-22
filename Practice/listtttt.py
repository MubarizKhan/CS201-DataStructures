class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
    
class List:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        print ("added to lost")
        temp.next = new_node

    def __str__(self):
        ret = "["
        temp = self.head
        while temp is not None:
            ret += str(temp.val) + ","
            temp = temp.next
        
        ret = ret.rstrip(',')
        ret += "]"

        return ret

    def insert(self,index, val):
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

        new_node.next = temp
        prev.next = new_node

    
    def remove_at(self, index):
        if self.head is None:
            raise Exception("List is empty, cant remove")

        if index == 0:
            self.head = self.head.next
            return

        counter = 0
        temp = self.head
        prev = temp

        while temp is not None and counter < index:
            prev = temp
            temp = temp.next
            counter += 1

        prev.next = temp.next
        return counter

    def remove(self, val):
        if self.head is None:
            raise Exception("List is empty, cant remove")

        if self.head.val == val:
            self.head = self.head.next
            return

        counter = 0
        temp = self.head
        prev = temp

        while temp is not None and temp.val != val:
            prev = temp
            temp = temp.next
            counter += 1

        prev.next = temp.next
        return counter

    def maximum(self):
        max = self.head.val
        temp = self.head

        while temp is not None:
            if temp.val > max:
                max = temp.val
            
            temp = temp.next

        print(max)
        return max

    def minimum(self):
        min = self.head.val
        temp = self.head

        while temp is not None:
            if temp.val < min:
                min = temp.val
            
            temp = temp.next

        print(min)
        return min
        
    # def rev(self)


    def get_last(self):
    
        if self.head is None:
            raise Exception("Empty")
        if self.head.next is None:
            return None

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        print (temp.val)
        return temp

    def len(self):
        temp = self.head
        counter = 0

        while temp is not None:
            
            temp = temp.next
            counter += 1

        return counter

    def reverse(self):
        if self.head is None:
            return

        if self.head.next is None:
            return None

        new_head = self.get_last()
        processing = new_head

        for i in range(self.len() - 1):
            temp = self.head
            while temp.next is not processing:
                temp = temp.next
            
            processing.next = temp
            processing = temp

        self.head.next = None
        self.head = new_head


    def append_list(self, list1):
        if self.head is None:
            self.head = list1.head
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = list1.head
        


    
L = List()
L.push(88)
L.push(99)
L.push(919)
L.push(101)

m = List()
m.push(11)
m.push(66)
    
print(L)

L.append_list(m)
# L.maximum()
# L.minimum()
# L.get_last()
# L.reverse()
print(L)