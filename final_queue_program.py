#Final Exam Question 2: -Ashfaq Ahmed
from queue import Queue #importing queue library

queue = Queue() #Creating a queue 
add = "Element 1" #defining element
queue.put(add) # Adiing element using the put method
pop = queue.get()

#displaying output
print("Queue :",add);
print("Popped Element :",pop);