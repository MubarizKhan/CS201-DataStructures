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

		temp.next = new_node
		# print ("inserted")

	def maximum(self):
		if self.head is None:
			raise Exception("Cannot find maximum as list is empty!")

		max = self.head.val
		min = self.head.val

		cur = self.head
		while cur is not None:
			if cur.val >= max:
				max = cur.val

			if cur.val <= min:
				min = cur.val

			cur = cur.next

		print ("the maximum in the List is: ", max)
		# print ("the miniimum in the List is: ", min)


	def minimum(self):
		if self.head is None:
			raise Exception("Cannot find maximum as list is empty!")

		min = self.head.val

		cur = self.head
		while cur is not None:
			
			if cur.val <= min:

				min = cur.val
			
			cur = cur.next

		print ("the miniimum in the List is: ", min)
		return min
		



	def remove(self, val):
		

		if self.head is None:
			raise Exception("the List is empty can't remove!")

		if self.head.val == val:
			sav = self.head.val
			self.head = self.head.next
			return sav

	
		temp = self.head
		prev = temp
		while temp is not None:
			if temp.val == val:
				ret = temp.val
				prev.next = temp.next
				return ret

			prev = temp
			temp = temp.next
			

	def __str__(self):
		ret = "["
		temp = self.head

		while temp is not None:
			ret += str(temp.val) + ","
			temp = temp.next

		ret = ret.rstrip(",")
		ret += "]"

		# print(ret)
		return ret


	def remove_min(self):
		y = self.minimum()
		# self.remove(self.minimum)
		self.remove(y)


	def len(self):
		temp = self.head
		counter = 0
		while temp is not None:
			counter += 1
			temp = temp.next

		print(counter)
		return counter


	def third_highest(self):

		len = self.len()

		if len < 3:
			return None


		h1 = self.head.val
		h2 = self.head.val
		h3 = self.head.val

		temp = self.head

		while temp is not None:
			if temp.val >= h1:
				h3 = h2
				h2 = h1
				h1 = temp.val

			elif temp.val > h2:
				h3 = h2
				h2 = temp.val

			elif temp.val > h3:
				h3 = temp.val

			temp = temp.next

		print(h3, "<-Third highest value! ")
		return(h3)


	def append_list(self, list2):
		if self.head is None:
			self.head = lis2.head

		temp = self.head
		while temp.next is not None:
			temp = temp.next

		temp.next = list2.head


	def operation_for_all(self):
		temp = self.head
		while temp.next is not None:
			temp.val *= 2
			temp = temp.next 





# Append one List to another
l = List()
l.push(1)
l.push(2)
l.push(3)
l.push(4)
l.push(5)

x = List()
x.push(6)
x.push(7)
x.push(8)
x.push(9)

# print(l)

# l.operation_for_all()

# l.append_list(x)
# print(l)

# l.third_highest()


# l.maximum()
# l.minimum()

# l.remove_min()
# l.remove(7)
# l.remove(1)
# l.remove(111)


print(l)


