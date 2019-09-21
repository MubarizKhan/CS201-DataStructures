class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Linkedlist:
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
            raise Exception("This list is empty, can't pop!")

        if self.head.next is None:
            ret = self.head.next.val
            self.head.next = None
            return

        temp = self.head
        prev = temp
        while temp.next is not None:
            prev = temp
            temp = temp.next

        ret = temp.val
        prev.next = None
        return ret



    def insert(self,index, val):
        new_node = Node(val)

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

        prev.next = new_node
        new_node.next = temp
        # temp.next = None

    def remove(self, val):
        if self.head is None:
            raise Exception("Listt is empty")

        if val == self.head.val:
            self.head = self.head.next



        temp = self.head
        counter_idx = 0
        prev = temp
        while temp is not None and temp.val == val:
            prev = temp 
            temp = temp.next
            counter_idx += 1

        num = temp.val
        prev.next = temp.next
        return (counter_idx, "<--index", num, "value removed")


    def len(self):
        if self.head is None:
            raise Exception("the List is empty")
        temp = self.head
        counter = 0

        while temp is not None:
            counter += 1
            temp = temp.next

        return counter

    def remove_at(self, index):
        temp = self.head
        prev = temp

        if self.head is None:
            raise Exception("List is empty! ")

        counter = 0
        while temp is not None and counter < index:
            prev = temp
            temp = temp.next 
            counter += 1

        prev.next = temp.next
        return counter 


    
    def maximum(self):
        if self.head is None:
            raise Exception("The list is empty!")

        max = self.head.val
        temp = self.head.next

        while temp is not None:
            if temp.val > max:
                max = temp.val

            temp = temp.next
        
        return max

    def minimum(self):
        if self.head is None:
            raise Exception("The list is empty")

        temp = self.head.next
        min = self.head.val

        counter = 0
        while temp is not None:
            if min > temp.val:
                min = temp.val

            temp = temp.next
            counter += 1

        return (min)
        
    def remove_min(self):
        if self.head is None:
            return None

        y = self.minimum()
        self.remove(y)


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

    def rev(self):
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
            processing = processing.next

        self.head.next = None
        self.head = new_head

    def get_counts(self):
        from collections import Counter
        cnt = Counter()
        
        temp = self.head
        while temp is not None:
            to_count = temp.val['age']
            cnt[to_count] += 1
            temp = temp.next

        return cnt.most_common()

        
    def append_list(self, lst):
        if self.head is None:
            self.head = lst.head
        
        # last = self.get_last()
        # last.next = lst.head
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = lst.head


    def so(self, fn):
        temp = self.head
        while temp is not None:
            print(fn(temp.val))
            temp = temp.next


if __name__ == '__main__': 
    L = Linkedlist()
    # L.push({'age': 15})
    #     # L.push("Frank ocean damn")
    # L.push({'age':45})
    # L.push({'age': 45})
    L.push(1)
    L.push(2)
    L.push(3)
    L.push(4)

    print(L)

    # L.get_counts()[0][0]
    # print(L.len())

    # L.insert(0,5)
    # L.insert(3,5555)
    # L.insert(5,6666)

    m = Linkedlist()
    m.push(123)
    m.push(123455)
    L.push(109)
    # print(L.third_highest(), "KK")
  
    # L.get_last()
    # L.rev()
    L.append_list(m)
    # L.pop()


    # from math import sqrt
    # L.so(sqrt)
    print(L)