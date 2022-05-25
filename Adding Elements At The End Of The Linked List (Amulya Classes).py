class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None
    def print_LL(self):
        if self.head==None:
            print("LinkedList Is Empty")
        else:
            while self.head is  not None:
                print(self.head.data)
                self.head=self.head.ref
    def add_end(self,data):
        new_Node=Node(data)
        if self.head==None:
            self.head=new_Node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_Node

l1=LinkedList()
l1.add_end(10)
l1.add_end(100)
l1.print_LL()