lst = [1, 2, "string", 1.0] # index starts at 0, list is mutable (can be modified later)
lst.append("hello world") # adds an item to the end of the list
value = lst.pop() # removes and returns the last item in the list
print(value)

lst.pop(1) # removes and returns item at index
lst.insert(0, "hi") # inserts a value at index
lst.remove("hi") # removes the first instance of given value

tple = (1, 2, 4)