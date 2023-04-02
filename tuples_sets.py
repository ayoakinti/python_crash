# A Tuple is a collection that is ordered and unchangeable. Allows duplicate members

# Create Tuple
fruits = ('Apples', 'Oranges', 'Grapes')
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

print(fruits, fruits2)

# Single value needs trailing comma
fruits3 = ('Apples',)
print(fruits3, type(fruits3))

print(fruits[1])

# Can't change value
# fruits[0] = 'Pears'

# Delete tuple
del fruits2

# Get length
print(len(fruits))

# print(fruits2)
 
# A Set is a collection which is unordered and indexed. No duplicate members

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

print(fruits_set)

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

# Add duplicate
fruits_set.add('Apples')

# Remove from set
fruits_set.remove('Grape')

# Clear set
fruits_set.clear()

# Delete
del fruits_set 

print(fruits_set)