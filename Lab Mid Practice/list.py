class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class linkedlist:
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

    def __str__(self):
        ret = '['
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
            shv = self.head.val
            self.head = None
            return shv

        temp = self.head
        prev = temp
        while temp.next is not None:
            prev = temp
            temp = temp.next

        val = temp.val
        prev.next = None
        return val

    def insert(self, index, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        
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

        new_node.next = temp
        prev.next = new_node
        
    def remove(self, val):
        if self.head is None:
            raise Exception("Nothing to remove")

        if self.head.val == val:
            self.head = self.head.next
            return

        temp = self.head
        prev = temp
        while temp is not None and temp.val is not val:
            # if temp.val is not val:
                prev = temp
                temp = temp.next
            # else:
        if temp is None:
            raise Exception("not found")
        tempsval = temp.val
        prev.next = temp.next
        return tempsval
        

    def len(self):
        temp = self.head
        counter = 0

        while temp is not None:
            counter += 1
            temp = temp.next

        return counter

    def minimum(self):
        if self.head is None:
            raise Exception("List is empty")

        min = self.head.val
        temp = self.head.next
        while temp is not None:
            if min > temp.val:
                min = temp.val
            temp = temp.next

        return min

    def remove_min(self):
        min = self.minimum()
        return self.remove(min)

    def get_last(self):
        temp = self.head
        while temp.next is not None:
            temp = temp.next 

        # print(temp.val)
        return temp

    def reverse(self):
        if self.head is None:
            return
        
        if self.head.next is None:
            return

        
        processing = self.get_last()
        new_head = processing

        for i in range( self.len() - 1):
            temp = self.head
            while temp.next is not processing:
                temp = temp.next

            processing.next = temp
            processing = processing.next

        self.head.next = None
        self.head = new_head

    def append_list(self, List):
        temp = self.head
        if self.head is None:
            self.head = List.head
            return

        while temp.next is not None:
            temp = temp.next
        
        temp.next = List.head

    def third_highest(self):
        h1 = self.head.val 
        h2 = self.head.val
        h3 = self.head.val

        temp = self.head
        while temp is not None:
            if temp.val >= h1:
                h3 = h2
                h2 = h1
                h1 = temp.val

            elif temp.val >= h2:
                h3 = h2
                h2 = temp.val
            
            elif temp.val >= h3:
                h3 = temp.val

            temp = temp.next

        return (h1, h2, h3)


              





ll = linkedlist()
ll.push(1)
ll.push(2)
ll.push(222)
ll.push(1466)

ll.insert(0, 0000)
ll.insert(3, 44)

print(ll)

print(ll.third_highest())
# ll.reverse()
# ll.remove(424)

# mm = linkedlist()
# mm.push(4)
# mm.push(88)
# mm.push(9808)

# ll.append_list(mm)


print(ll)