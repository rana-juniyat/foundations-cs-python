# Function to add two matrices
def add_matrices():
    #Get the matrix dimentions (row and columns)
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of culomns: "))

    #initialize two matrices
    matrix1 = []
    matrix2 = []

    #prompt for the first matrix elements
    print("Enter elements of the first matrix:")
    for _ in range(rows):
        row = []
        for _ in range(columns):
            element = int(input("enter an element: "))
            row.append(element)
        matrix1.append(row)
     
    #prompt for the first matrix elements
    print("Enter elements of the second matrix:")
    for _ in range(rows):
        row = []
        for _ in range(columns):
            element = int(input("enter an element: "))
            row.append(element)
        matrix2.append(row)

    #perform matrix addition
    result_matrix = []
    for i in range(rows):
        result_row=[]
        for j in range(columns):
             result_row.append(matrix1[i][j]+matrix2[i][j])
        result_matrix.append(result_row)

    # Display the matrices and their addition result
    print("Matrix 1:")
    for row in matrix1:
        print(row)

    print("Matrix 2:")
    for row in matrix2:
        print(row)

    print("Matrix 1 + Matrix 2:")
    for row in result_matrix:
        print(row)        

#################################################################################################

#Function to check if one matrics is rotation of another
def check_rotation():
    # Get the dimentions (rows and columns) of the first matrix
    rows1 = int(input("Enter the number of rows in the first matrix: "))
    columns1 = int(input("Enter the number of culomns in the first matrix: "))

    #initialize the first matrix
    matrix1 = []
    print("Enter elements of the first matrix:")
    for _ in range(rows1):
        row = []
        for _ in range(columns1):
            element = int(input("enter an element: "))
            row.append(element)
        matrix1.append(row) 

    # Get the dimentions (rows and columns) of the first matrix
    rows2 = int(input("Enter the number of rows in the second matrix: "))
    columns2 = int(input("Enter the number of culomns in the second matrix: "))

    #initialize the second matrix
    matrix2 = []
    print("Enter elements of the second matrix:")
    for _ in range(rows2):
        row = []
        for _ in range(columns2):
            element = int(input("enter an element: "))
            row.append(element)
        matrix2.append(row)

    # Check if one matrix is a rotation of the other
    if rows1==columns2 and rows2==columns1:
        #Transpose the first matrix to check if it matches the second matrix
        transpose_matrix1=[]
        for i in range(columns1):
            row = []
            for j in range(rows1):
                row.append(matrix1[j][i])
            transpose_matrix1.append(row)
        
        if transpose_matrix1 == matrix2:
            print("The second matrix is a rotation of the first matrix.")
        else:
            print("The second matrix is not a rotation of the first matrix.")

    else:
        print("The matrices cannot be compared for rotation")
##################################################################################################

#Function to creat and invert a dictionary
def invert_dictionary():
    #Initialize an empty dictionary
    original_dict = {}

    #prompt the user to add key-value pairs to the dictionary
    while True:
        key=input("Enter a key for (or 'done' to finish):")
        if key=='done' :
            break
        value = input("Enter a value: ")
        original_dict[key] = value

    #Invert the dictionary
    inverted_dict = {}
    for key,value in original_dict.items():
        if value in inverted_dict:
            if isinstance(inverted_dict[value], list):
                inverted_dict[value].append(key)
            else:
                inverted_dict[value] = [inverted_dict[value], key]
        else:
            inverted_dict[value] = key

    # Display the original and inverted dictionaries
    print("Before inverting:")
    print(original_dict)
    print("After inverting:")
    print(inverted_dict)

##################################################################################################

# Function to create a user data matrix and convert it into a dictionary
def convert_matrix_to_dict():
    user_data_matrix = []

    # Prompt the user to enter user data in the matrix
    while True:
        user_data = input("Enter user data (First Name, Last Name, ID, Job Title, Company), or 'done' to finish: ")
        if user_data == 'done':
            break
        user_data_list = user_data.split(", ")
        if len(user_data_list) != 5:
            print("Invalid input. Please enter data in the format 'First Name, Last Name, ID, Job Title, Company'.")
            continue
        user_data_matrix.append(user_data_list)

    # Convert the matrix into a dictionary
    user_dictionary = {}
    for user in user_data_matrix:
        user_id = user[2]  # ID is the third element
        user_info = [user[0], user[1], user[3], user[4]]  # First Name, Last Name, Job Title, Company
        user_dictionary[user_id] = user_info

    # Display the user dictionary
    print("User Dictionary:")
    print(user_dictionary)
    
##################################################################################################

# Recursive function to check if a string is a palindrome
def check_palindrome():
    # Base case: an empty string or a string with one character is always a palindrome
    if len(s) <= 1:
        return True

    # Compare the first and last characters of the string
    if s[0] == s[-1]:
        # Recursively check the rest of the string (excluding the first and last characters)
        return check_palindrome(s[1:-1])

    # If the first and last characters do not match, it's not a palindrome
    return False

# Prompt the user for a string
user_input = input("Enter a string: ")

# Remove spaces and convert to lowercase for case-insensitive comparison
user_input = user_input.replace(" ", "").lower()

# Check if the input string is a palindrome
if check_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


##################################################################################################

# Main function
def main():
  # Get the user's name
    user_name = input("Enter your name: ")
    print(f"Welcome, {user_name}!")

    while True:
        print("\nMenu:")
        print("1. Add Matrices")
        print("2. Check Rotation")
        print("3. Invert Dictionary")
        print("4. Convert Matrix to Dictionary")
        print("5. Check Palindrome")
        print("6. Search for an Element & Merge Sort")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_matrices()
        elif choice == "2":
            check_rotation()
        elif choice == "3":
            invert_dictionary()
        elif choice == "4":
            convert_matrix_to_dict()
        elif choice == "5":
            check_palindrome()
        elif choice == "6":
            search_and_merge_sort()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-7).")

if __name__ == "__main__":
     main()