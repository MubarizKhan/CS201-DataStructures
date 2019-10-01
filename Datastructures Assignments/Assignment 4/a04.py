class Node:
     def __init__(self, val):
         self.val = val
         self.next = None


class Ring:
    def __init__(self):
        self.head = None
    def __str__(self):
        ret_str = "["
        temp = self.head
        while temp is not None:
            ret_str += str(temp.val) + ","
            temp = temp.next

            if temp == self.head:
                break
        
        ret_str = ret_str.rstrip(",")
        ret_str += "]"
        return ret_str

    def _get_last(self):
        temp = self.head
        if self.head is None:
            return None

        temp = self.head.next
        while temp.next is not self.head:
            temp = temp.next

        return temp


    def insert(self,index, val):
        new_node = Node(val)
        last = self._get_last()

        if index == 0:
            new_node.next = self.head
            self.head = new_node

            if last is None:
                self.head.next = self.head
            else:
                last.next = new_node
            

            return

        if self.head is None and index > self.len():
            self.head = new_node
            new_node.next = self.head
            return


        temp = self.head
        prev = temp
        counter = 0
        
        while temp is not None and counter < index:
            prev = temp
            temp = temp.next
            counter += 1

        prev.next = new_node
        new_node.next = temp
        return


    def remove(self,val):
        if self.head is None:
            raise Exception("The list is empty!")

        temp = self.head
        last = self._get_last()

        if temp.val == val:
            if last == self.head:
                self.head = None
                return
            
            self.head = temp.next
            last.next = self.head
            return

        prev = temp
        temp = temp.next

        while temp is not self.head:
            # temp = temp.next
            if temp.val == val:
                break

            prev = temp
            temp = temp.next

        if temp == self.head:
            return

        prev.next = temp.next



    def remove_at(self, index):
        temp = self.head
        last = self._get_last()


        if index == 0:
            if last == self.head:
                self.head = None
                return
            
            temp = temp.next
            self.head = temp
            return
            # last.next = self.head

        counter = 0
        
        prev = temp
        while temp is not last and counter < index:
            prev = temp
            temp = temp.next
            counter += 1


        prev.next = temp.next
        temp = None
        return



    def len(self):

        temp = self.head
        last = self._get_last() 

        if self.head is None:
            return 0
            raise Exception("This list is empty!")

        if last == self.head:
            return 1
            
        count = 0
        while temp is not last :
            temp = temp.next
            count += 1

        count += 1

        return count


    def get(self, index):
        temp = self.head
        last = self._get_last()

        if self.head is None:
            raise IndexError("The list is empty")

        counter = 0
        while temp is not last and counter < index:
            prev = temp
            temp = temp.next
            counter += 1

        return temp.val

    
    def push(self, val):

        # new_node = Node(val)
        # if self.head == None:
        #     self.head = new_node
        #     new_node.next = self.head
        #     return

        # temp = self.head
        # while temp.next is not self.head:
        #     temp = temp.next


        # new_node.next = self.head
        # temp.next = new_node

        length = self.len()
        return self.insert(length, val)
       

    def pop(self):
        last = self._get_last()
        temp = self.head

        l = self.len()

        val = self.get(l)
        return self.remove_at(val - 1)

        





    





if __name__ == '__main__': 
    r = Ring()
    # r.insert(1, 1)
    # r.insert(0, 1)
    # r.insert(0, 2)
    # r.insert(1, 3)
    # r.insert(7, 5)  # different behavrior since it's a ring!
    # 

    r.push(1)
    r.push(23)
    r.pop()
    r.pop()

    print(r.len()) 

    
    print(r)
