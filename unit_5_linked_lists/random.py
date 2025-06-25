class Node:
    def __init__(self,val:int) -> None:
        self.val = val
        self.next = next

class LinkedList:
    def __init(self):
        self.head = None
        self.tail = None
        self.head.next= self.tail
        self.tail.next = self.head

    def get(self,index:int)-> int:
        temp_node = self.head
        while index > 0:
            temp_node = temp_node.next
        return temp_node

    def insertHead(self,val:int) -> None:
        temp_node = Node(val)
        temp_node = self.head
        self.head = self.head.next
        self.tail.next = temp_node

    def insertTail(self,val: int) -> None:
        temp

    def remove(self, index: int) -> bool:
        pass

    def getValues(self) -> List[int]:
        pass


"""
iterate for n amount of times
"""