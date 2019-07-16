"""

A) Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
"""

list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print ("A: ")
for l in list:
    if l < 5:
        print (l)

"""
Extras:

B) Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
"""

list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

list_2 = []

for l in list:
    if l < 5:
        list_2.append(l)

print ("B: ",list_2)

"""
C) Write this in one line of Python.
"""

list_3 = [l for l in list if l < 5]


print ("C: ",list_3)


"""
Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
"""


input = input("Please enter a number: ")

list_4 = []

for l in list:
    if l < int(input):
        list_4.append(l)

print("D: ",list_4)
