class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class CLL:
    def __init__(self):
        self.head = None
    
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

            if last == None:
                self.head.next = self.head
            else:
                last.next = new_node

            return
        
        temp = self.head
        counter = 0
        prev = temp
        while temp.next is not self.head and counter < index:
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

    def remove(self, val):
        if self.head is None:
            raise Exception("List is empty!")

        temp = self.head
        last = self.get_last

        if temp.val == val:
            if last == self.head:
                self.head = None
            else:
                self.head = temp.next
                last.next = self.head


            return


        prev = temp 
        temp = temp.next

        while temp is not self.head:
            if temp.val == val:
                break

            prev = temp
            temp = temp.next

        if temp == self.head:
            return 

        prev.next = temp.next





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

cll.remove(9999)

print(cll)