#Asmaa Hussein Omar 20231021
#Roaa mohammed Sayed20230142
#Amany Hussein Mousa 20231026
# Function for binary addition
def binary_addition():
    first_number = input("Input the first number: ")
    second_number = input("Input the second number: ")

    # Find the maximum length to align numbers
    if len(first_number) >= len(second_number):
        max_range = len(first_number)
    else:
        max_range = len(second_number)
    """#####     01101 + 10111 = 100100 ==> overflow     #####"""
    # Check if each digit is a valid binary digit (0 or 1)
    for i in range(max_range - 1, -1, -1):
        if first_number[i] != '1' and first_number[i] != '0' or second_number[i] != '1' and second_number[i] != '0':
            print('Invalid input, please enter a valid binary number')
            return False

    len_first = len(first_number)
    len_second = len(second_number)

    # Make both numbers of equal length by adding leading zeros
    while len(first_number) > len(second_number):
        second_number = "0" + second_number
    while len(second_number) > len(first_number):
        first_number = "0" + first_number

    result = ''
    carry = 0

    # Perform binary addition
    for i in range(max_range - 1, -1, -1):
        if int(first_number[i]) + int(second_number[i]) + carry == 0:
            result = '0' + result
            carry = 0
        elif int(first_number[i]) + int(second_number[i]) + carry == 1:
            result = '1' + result
            carry = 0
        elif int(first_number[i]) + int(second_number[i]) + carry == 2:
            result = '0' + result
            carry = 1
        elif int(first_number[i]) + int(second_number[i]) + carry == 3:
            result = '1' + result
            carry = 1

    # If there is a carry after the loop, add it
    if carry == 1:
        result = "1" + result

    # Print the result of binary addition
    print(f"{first_number} + {second_number} = {result}")


# Function for binary subtraction
def binary_subtraction():
    first_number = input("Input the first number: ")
    second_number = input("Input the second number: ")

    # Determine the maximum length of the binary numbers
    if len(first_number) >= len(second_number):
        max_range = len(first_number)
    else:
        max_range = len(second_number)

    for i in range(max_range - 1, -1, -1):
        if first_number[i] != '1' and first_number[i] != '0' or second_number[i] != '1' and second_number[i] != '0':
            print('Invalid input, please enter a valid binary number')
            return False

    # Store the original lengths for later use
    len_first = len(first_number)
    len_second = len(second_number)

    # Make the binary numbers of equal length by padding with zeros
    while len(first_number) > len(second_number):
        second_number = "0" + second_number
    while len(second_number) > len(first_number):
        first_number = "0" + first_number

    result = ''
    borrow = 0

    # Iterate over each bit from right to left

    """#####   01001 - 00111 = 00010   #####"""

    for i in range(max_range - 1, -1, -1):
        # Get the current bits of the binary numbers
        bit1 = int(first_number[i])
        bit2 = int(second_number[i])
        # Calculate the difference between the bits and consider the borrow
        difference = bit1 - bit2 - borrow
        # If the difference is negative, adjust and set borrow to 1
        if difference < 0:
            difference += 2
            borrow = 1
        else:
            borrow = 0
        # Append the current bit of the result to the left
        result = str(difference) + result

    # If there's a remaining borrow, append it to the left
    if borrow == 1:
        result = '1' + result

    # Print the result of binary subtraction
    print(f"{first_number} - {second_number} = {result}")


# Function to calculate the first complement of a binary number
def first_complement():
    num = input("Enter a binary number: ")
    my_list = []

    """#####     1110 ==>> 0001    #####"""

    # Check if each digit is a valid binary digit (0 or 1)
    for i in range(len(num)):
        if num[i] != '1' and num[i] != '0':
            print('Invalid input, please enter a valid binary number')
            return False

        # If the user input a binary number, compute its complement
        my_list.append('1' if num[i] == '0' else '0')

    # Print the result of the first complement
    print('1s complement:', ''.join(my_list))

    # Return the result as a string
    return ''.join(my_list)


# Function to calculate the second complement
def second_complement():
    # Calculate the first complement
    first_number = first_complement()

    """#####  000011 ===>> 111101  #####"""

    # Initialize the second number for binary addition
    second_number = "1"

    # Ensure both numbers are of equal length by adding leading zeros
    while len(first_number) > len(second_number):
        second_number = "0" + second_number
    while len(second_number) > len(first_number):
        first_number = "0" + first_number

    result = ''
    carry = 0
    max_range = len(first_number)

    # Perform binary addition (which is equivalent to the second complement)
    for i in range(max_range - 1, -1, -1):
        if int(first_number[i]) + int(second_number[i]) + carry == 0:
            result = '0' + result
            carry = 0
        elif int(first_number[i]) + int(second_number[i]) + carry == 1:
            result = '1' + result
            carry = 0
        elif int(first_number[i]) + int(second_number[i]) + carry == 2:
            result = '0' + result
            carry = 1
        elif int(first_number[i]) + int(second_number[i]) + carry == 3:
            result = '1' + result
            carry = 1

    # If there is a carry after the loop, add it
    if carry == 1:
        result = "1" + result

    # Print the result of the second complement
    print("Second complement:", result)


# Main binary calculator function
def binary_calculator():
    while True:
        # Display main menu
        print("** Binary Calculator **")
        print("A) Insert new numbers")
        print("B) Exit")

        # Get user's choice for main menu
        choice1 = input("Enter your choice: ").lower()

        # Check the user's choice for main menu
        if choice1 == 'a':
            # Display submenu for operations
            print("** Please select the operation **")
            print("A) Compute one's complement")
            print("B) Compute two's complement")
            print("C) Addition")
            print("D) Subtraction")

            # Get user's choice for the specific operation
            choice2 = input("Enter your choice: ").lower()

            # Check the user's choice for the specific operation
            if choice2 == 'a':
                # Compute and print the first complement
                result = first_complement()
            elif choice2 == 'b':
                # Compute and print the second complement
                second_complement()
            elif choice2 == 'c':
                # Perform and print binary addition
                binary_addition()
            elif choice2 == 'd':
                # Perform and print binary subtraction
                binary_subtraction()
            else:
                # Invalid choice for the specific operation
                print("Please select a valid choice.")
                continue
        elif choice1 == 'b':
            # Exit the program
            print("Exiting program. Goodbye!")
            break
        else:
            # Invalid choice for main menu
            print("Please select a valid choice.")
            continue

# Call the main binary calculator function
binary_calculator()
