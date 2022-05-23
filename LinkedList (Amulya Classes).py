class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None
    def PrintLinkedList(self):
        s=""
        if self.head is None:
            print("LinkedList Is Empty")
        else:
            while self.head is not None:
                s+=str(self.head.data)+"->"
                self.head=self.head.ref
            print(s)
            
    def add(self,data):
        a=Node(data)
        a.ref=self.head
        self.head=a
        
l1=LinkedList()
l1.add(101)
l1.add(102)
l1.PrintLinkedList()