class Stack:

  def __init__(self):
    #CREATE AN EMPTY stack
    #put the front at index 0
    #back at index n - 1
    self.my_stack = []

  #ADDS and item to the back of the stack
  #If the back is at index n - 1
  def enstack(self, item):
    self.my_stack.append(item)

  #Remove the item at the front
  def destack(self):
    #write the code for destack
    self.my_stack.pop(0)

  #Look at the item at the item at the front
  def front(self):
    return self.my_stack[0] 