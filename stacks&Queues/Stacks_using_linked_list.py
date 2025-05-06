class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    
class Stack:
    # Initialization
    def __init__(self):
        self.top=None
        self._size=0
    
    #Check if stack is empty
    def is_empty(self):
        return self.top is None
    
    #Push to stack
    def push(self,value):
        new_node=Node(value)
        new_node.next=self.top
        self.top=new_node
        self._size+=1
    
    # Pop to stack
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        popped_value=self.top.value
        self.top=self.top.next
        self._size-=1
        return popped_value
    # Top value of stack
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.top.value

    @property
    def size(self):
        return self._size

    def display(self):
        current = self.top
        print("Stack(top->bottom):", end=" ")
        while current:
            print(current.value,end=" ")
            current=current.next
        print()

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()

print(stack.pop())
print(stack.peek())
print(stack.size) 
stack.display()        