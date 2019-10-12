class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class CLL:
    def __init__(self):
        self.head = None

    def push(self, val):

        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            print("Reached here")
            return
        
        temp = self.head

        while temp.next is not self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head
        print("Reached here xx")
        return

    def pop(self):
        if self.head is None:
            raise Exception("List is emmpty!")

        temp = self.head
        prev = temp
        while temp.next is not self.head:
            prev = temp
            temp = temp.next
        
        prev.next = temp.next
        # tempsval = temp.val

    def get_last(self):

        if self.head is None:
            return None

        temp = self.head
        while temp.next is not self.head:
            temp = temp.next
        
        return temp

    
    def insert(self, index, val):
        
        new_node = Node(val)
        last = self.get_last()

        if index == 0:
            new_node.next = self.head
            self.head = new_node

            if last is None:
                self.head.next = self.head
            else:
                last.next = new_node

            return

        temp = self.head
        counter = 0
        while temp is not None and counter < index:
            prev = temp
            temp = temp.next
            counter += 1

        prev.next = new_node
        new_node.next = temp





        

            
        
    

    def __str__(self):
        ret = "["
        temp = self.head
        while temp is not None:
            ret += str(temp.val) + ","
            temp = temp.next

            if temp == self.head:
                break

        ret = ret.rstrip(",")
        ret += "]"

        return ret




cll = CLL()
# cll.push(11)
# cll.push(22)
# cll.push(3)
# cll.push(99)
# cll.push(2)

print (cll)

cll.insert(0, 232)
cll.insert(1, 22)
cll.insert(2, 9999)

print(cll)
