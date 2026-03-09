# Create a Lists of Fruits
fruits = ["Apple","Banana","Mango","Orange","Cherry"]

# Access list elements
print("Original list:", fruits)
print("First fruit:", fruits[0])
print("Third fruit:", fruits[2])

# Add elements to the list
fruits.append("Pineapple")   # Add at end
fruits.insert(1, "Papaya")   # Add at specific position
print("After adding fruits:", fruits)

# Remove elements from the list
fruits.remove("Banana")      # Remove specific fruit
fruits.pop()                 # Remove last fruit
print("After removing fruits:", fruits)

# Sort list elements
fruits.sort()
print("Sorted list:", fruits)

# Reverse list elements
fruits.reverse()
print("Reversed list:", fruits)