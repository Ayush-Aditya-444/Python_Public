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

l1=LinkedList()
l1.add_after(10,2)
l1.print_LL()