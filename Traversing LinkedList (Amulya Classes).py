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
l1=LinkedList()
l1.print_LL()