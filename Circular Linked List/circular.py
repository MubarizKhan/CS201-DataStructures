class Node:
    def __init__(self,val):
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
            return
        
        temp = self.head
        while temp.next is not self.head:
            temp = temp.next

            if temp.next == self.head:
                break

        temp.next = new_node
        new_node.next = self.head

    def get_last(self):
        temp = self.head
        while temp.next is not self.head:
            temp = temp.next

        # print (temp.val)
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

        if self.head is None:
            raise Exception("List is empty!")

        temp = self.head
        prev = temp
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

    def remove(self, val):
        if self.head is None:
            return None

        temp = self.head
        last = self.get_last()

        if temp.val == val:
            if last == self.head:
                self.head = None
            
            else:
                self.head = temp.next
                last.next = self.head
            return

        prev = temp
        temp = temp.next

        while temp != self.head:
            if temp.val == val:
                break

            prev = temp
            temp = temp.next

        if temp == self.head: #not found
            return

        prev.next = temp.next

            


cll = CLL()

cll.push(12)
cll.push(5)
cll.push(1)
cll.push(78)

cll.insert(0, 71)
cll.insert(2, 4)


print(cll)

cll.remove(71)
cll.remove(78)


print(cll)
        
