# Final Exam Question 3: Priority Queue Operations
# Create a Priority Queue, add an element, pop an element, and display the output.

#importing the library
from queue import PriorityQueue

#Creating a Priority Queue
priorityqueue = PriorityQueue()

#Adding an element to the Priority Queue
add = "Ashfaq Ahmed's Priority Item"
priority_state = 2  # Priority level (lower number indicates higher priority)
priorityqueue.put((priority_state, add))

#Popping an element from the Priority Queue
popelement = priorityqueue.get()[1]  # Extracting the actual element from the tuple

#Displaying the unique output
print("Welcome to the Final Exam!")
print("I am required to perform the following Priority Queue operations:")
print("1. Adding the following item to the Priority Queue: ", add,  "with priority state :",priority_state)
print("2. Popping the highest priority item from the Priority Queue.")
print("\nExecuting operations...\n")

#Displaying the output
print("Priority Queue Operations Completed:")
print("Added Element: ",add, "Priority Level: ",priority_state)
print("Popped Element: ",popelement)
print("\nThank you!")
