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

    def add_begin(self,data):
        new_Node=Node(data)
        new_Node.ref=self.head
        self.head=new_Node 

    def add_end(self,data):
        new_Node=Node(data)
        if self.head==None:
            self.head=new_Node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_Node
    
    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print("Node Is Not Present In The LinkedList")
        else:
            new_Node=Node(data)
            new_Node.ref=n.ref
            n.ref=new_Node
    
    def add_before(self,data,x):
        if self.head==None:
            print("Linked List is Empty")
            return
        if self.head.data==x:
            new_Node=Node(data)
            new_Node.ref=self.head
            self.head=new_Node
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n is None:
            print("Node Is Not Found")
        else:
            new_Node=Node(data)
            new_Node.ref=n.ref
            n.ref=new_Node

l1=LinkedList()
l1.add_begin(103)
l1.add_begin(102)
l1.add_begin(100)
l1.add_end(110)
l1.add_end(111)
l1.add_end(112)
l1.add_before(106,107)
l1.add_before(105,106)
l1.add_before(104,105)
l1.add_after(107,103)
l1.add_after(108,107)
l1.add_after(109,108)

l1.PrintLinkedList()