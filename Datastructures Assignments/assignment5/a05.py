class Node:
    def __init__(self, data=None):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        ret = "["
        temp = self.head

        if self.head is None:
            print ("The list is empty")
            return
        
        while temp is not None:
            ret += str(temp.val) + ","
            temp = temp.next

        ret= ret.rstrip(", ")
        ret += "]"
        return ret

    def __str__(self):
        ret = "["
        temp = self.head

        while temp is not None:
            ret += str(temp.val) + ","
            temp = temp.next

        ret = ret.strip(",")
        ret += "]"
        return ret 

    
    def push(self,val):
        new_node = Node(val)
        temp = self.head

        if self.head is None:
            self.head = new_node
            return
        
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    def insert(self, index, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node

        if index == 0:
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

        temp.next = new_node

    def pop(self):
        if self.head is None:
            raise Exception("The list is empty can't pop!")

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next is not None:
            prev = temp 
            temp = temp.next

        pop_val = prev.next.val
        prev.next = None
        return pop_val


    def remove(self, val):
        # new_node = Node(val)
        if self.head is None:
            raise Exception("The list is empty can't remove!")

        temp = self.head
        if temp.val == val:
            if temp.next is None:
                self.head = None
                return 
            
            self.head = self.head.next
            return

        while temp.val is not val:
            prev = temp
            temp = temp.next

        prev.next = temp.next

        
    def remove_at(self, index):
        if self.head is None:
            raise Exception("The list is empty, can't remove!")

        temp = self.head
        prev = temp
        counter = 0

        if index == 0:
            self.head = self.head.next
            return 

        while temp.next is not None and counter <= index:
            prev = temp 
            temp = temp.next
            counter += 1

        prev.next = temp.next


    def len(self):
        if self.head is None:
            raise Exception("The list is empty")

        temp = self.head
        counter = 0
        while temp is not None:
            temp = temp.next
            counter += 1

        print (counter)
        return counter 

    def get_last(self):
        if self.head is None:
            raise Exception("List is empty! ")

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        return temp  

    def reverse_list(self):

        if self.head is None:
            return


        temp = self.head
        rep = temp 
        l = self.get_last()

        while temp.next is not None:
            v = temp
            while v is not None:
                x = temp.val
                temp.val = v.val 
                v.val = x
                v = v.next


            temp = temp.next











if __name__ == '__main__': 
    l = LinkedList() 
    l.push(1) 
    l.push(2)
    # l.push(3)
    # l.push(4)
    # l.push(5)
    
    print(l)

    

    l.reverse_list() 
    print(l)
    

