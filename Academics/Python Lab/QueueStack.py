class Queue:
    def __init__(self):
        self.left=None
        self.value=None
        self.right=None
        self.front=None
    def insert(self,v):
        if(self.value==None):
         self.value=v
         self.front=self.left=self
         return
        element=Queue()
        element.value=v
        self.front.right=element
        self.front=element
    def delete(self):
        if(self.left==None):
            print("Queue is empty")
            return
        print(self.left.value)
        self.left=self.right
    def display(self):
        if (self.left == None):
            print("Queue is empty")
            return
        element=self.left
        while(element!=None):
            print(element.value,end=',')
            element=element.right
        print()
class Stack:
    def __init__(self):
        self.next=None
        self.value=None
        self.top=None
    def push(self,v):
        if(self.top==None):
         self.value=v
         self.top=self
         return
        element=Stack()
        element.value=v
        element.next=self.top
        self.top=element
    def pop(self):
        if(self.top==None):
            print("Stack is empty")
            return
        print(self.top.value)
        self.top=self.top.next
    def display(self):
        if (self.top == None):
            print("Stack is empty")
            return
        element=self.top
        while(element!=None):
            print(element.value,end=',')
            element=element.next
        print()
o=Stack()
o.push(1)
o.push(2)
o.push(3)
o.push(6)
o.pop()
o.display()
q=Queue()
q.insert(11)
q.insert(2)
q.insert(3)
q.insert(1)
q.delete()
q.display()


