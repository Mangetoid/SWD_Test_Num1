# Create an empty array
my_array = []

# Loop until the user enters a non-integer value
while True:
    try:
        # Get user input as an integer
        num = int(input("Enter an integer (or any non-integer value to exit): "))
        
        # Append the integer to the array
        my_array.append(num)
    except ValueError:
        # Exit the loop if a non-integer value is entered
        break

# Print the array
print("Array:", my_array)

# Initialize variables
max_value = my_array[0]  # Assume the first element is the maximum
max_index = 0

# Iterate through the array starting from the second element
for i in range(1, len(my_array)):
    if my_array[i] > max_value:
        # Update the maximum value and its index
        max_value = my_array[i]
        max_index = i

# Print the maximum value and its index
print("Maximum value:", max_value)
print("Index of maximum value:", max_index)
