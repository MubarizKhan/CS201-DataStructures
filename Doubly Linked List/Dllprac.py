class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DLL:
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
            raise Exception("List is empty!")

        if self.head.next is None:
            val = self.head.val
            self.head = None
            return val

        temp = self.head
        prev = temp
        while temp.next is not None:
            prev = temp
            temp = temp.next
        val = temp.val
        prev.next = None
        temp.prev = None

        return val


    def insert(self, index, val):
        new_node = Node(val)
        if index == 0:
            new_node.next = self.head

            if self.head is not None:
                self.head.prev = new_node

            self.head = new_node
            return

        

        temp = self.head
        prev = temp
        counter = 0
        while temp is not None and counter < index:
            prev = temp
            temp = temp.next
            counter += 1


        prev.next = new_node
        new_node.prev = prev

        new_node.next = temp
        if temp is not None:
            temp.prev = new_node

        return counter

    # def reverse(self):
    #     if self.head is None:
    #         raise Exception("List is empty")

    #     temp = self.head 
    #     prev = temp
    #     while temp is not None:





l = DLL()
l.push(1)
l.push(2)
l.push(3)

print(l)

l.insert(2, 9 )
print(l)
l.insert(3, 44)
print(l)
l.insert(6, 666)
# l.pop()
# l.pop()
# l.pop()
# l.pop()

print(l)