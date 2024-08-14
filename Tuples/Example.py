""" WAP to count the no.of students with A grade in the following tuple"""

Grades = ("B", "A", "C", "D", "A", "E", "A", "C", "A")
print(Grades.count("A"))    #Output: 4

""" IMPORTANT: Tuples are Immutable in python 
        But we can modify them by coverting
        tuple into list
"""
a = ("apple", "banana", "orange")   #Tuple
b = list(a)     #Tuple converted into list
b[1] = "watermelon"     #value modified
a = tuple(b)

print(a)    #Output: 'apple', 'watermelon', 'orange'
