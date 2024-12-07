# LIST
# 1) Create a list of 5 random numbers and print the list
a=[1, 4, 6, 11, 15]
print(a)

# 2) Insert 3 new values to the list and print the updated list
a.extend([20,3,19])
print(a)

# 3) Use a for loop to print each element in the list
for element in a:
    print(element)
    
# DICTIONARY
# 1) Creating the dictionary
d = {'name': 'John', 'age': 25, 'address': 'New York'}
print(d)

# 2) Adding a new key-value pair to the dictionary
d['phone'] = '1234567890'
print(d)
    
# SET
# 1) Creating the set
b = {1, 2, 3, 4, 5}
print(b)

# 2) Adding the value 6 to the set
b.add(6)
print(b)

# 3) Removing the value 3 from the set
b.remove(3)
print(b)

# TUPLE    
# 1) Create a tuple with values 1, 2, 3, and 4
t1 = (1, 2, 3, 4)
print(t1)

# 2) Length of the tuple
print(len(t1))