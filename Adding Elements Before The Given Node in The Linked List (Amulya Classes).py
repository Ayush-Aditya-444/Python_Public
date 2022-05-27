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
    
    def add_end(self,data,x):
        if self.head==None:
            print("Linked List is Empty")
        if self.data.head==x:
            new_Node=Node(data)
            new_Node.ref=self.head
            self.head=new_Node
            return
        n=self.head
        while n is not None:
            if self.head==x:
                break
            n=n.ref


l1=LinkedList()
l1.print_LL()