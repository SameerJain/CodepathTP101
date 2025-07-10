class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

head = Node(4,Node(3,Node(2,None)))

print(head.value, head.next.value, head.next.next.value)





