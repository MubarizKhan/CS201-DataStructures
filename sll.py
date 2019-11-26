class node:
    def __init__(self, val):
        self.val = val
        self.next = None
class ll:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = node(val)

        if self.head is None:
            self.head = new_node
            print("self.head was none")
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        print("inserted")
        temp.next = new_node

    
    def __str__(self):
        temp = self.head
        ret = "["
        while temp is not None:
            ret += str(temp.val) + ","
            temp = temp.next

        ret = ret.rstrip(",")
        ret += "]"
        return ret

    def delete(self, val):
        temp = self.head
        # prev = temp
        if temp is not None:
            if temp.val == val:
                self.head = temp.next
                return

        while temp is not None:
            if temp.val == val:
                break
            
            prev = temp
            temp = temp.next

        if temp is None:
            print ("value not found")
            return

        prev.next = temp.next

    def merge_list(self, l2):
        if self.head is None:
            self.head = l2.head

        temp = self.head
        while temp is not None:
            temp = temp.next
        print(temp.val)
        temp.next = l2.head

    def find_min(self):
        if self.head is None:
            raise Exception(">")

        min = self.head.val
        temp = self.head.next
        while temp is not None:
            if temp.val < min:
                min = temp.val

            temp = temp.next
        return min
        # print(temp.val)

    def get_last(self):
        temp = self.head
        if temp is None:
            return
        
        while temp.next is not None:
            temp = temp.next

        return temp

    def len_(self):
        if self.head is None:
            return

        if self.head.next is None:
            return 1

        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next

        return count

    def rev(self):
        if self.head is None:
            return

        if self.head.next is None:
            return

        new_head = self.get_last()
        proc = new_head
        

        for i in range(self.len_() - 1):
            temp = self.head

            while temp.next != proc:
                temp = temp.next

            proc.next = temp
            proc = proc.next

        self.head.next = None
        self.head = new_head

    


ll = ll()
lst = [1,2,3,4,5,6,7,8]


for i in lst:
    ll.push(i)

print(ll.len_())
ll.rev()
print(ll)



    

        
