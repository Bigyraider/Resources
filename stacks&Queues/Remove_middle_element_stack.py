# Standalone Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Stack using linked list
class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        popped = self.top.value
        self.top = self.top.next
        self._size -= 1
        return popped

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.top.value

    def is_empty(self):
        return self.top is None

    def size(self):
        return self._size

    def display(self):
        current = self.top
        print("Stack (top -> bottom):", end=" ")
        while current:
            print(current.value, end=" ")
            current = current.next
        print()



def delete_middle(stack):
    def delete_helper(current_index, target_index):
        if current_index == target_index:
            stack.pop()
            return
        temp = stack.pop()
        delete_helper(current_index + 1, target_index)
        stack.push(temp)

    if stack.is_empty():
        return

    mid_index = stack.size() // 2
    delete_helper(0, mid_index)
