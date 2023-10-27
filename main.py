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
    result = [[0]*columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    # Display the matrices and their addition result
    print("Matrix 1:")
    for row in matrix1:
        print(row)

    print("Matrix 2:")
    for row in matrix2:
        print(row)

    print("Matrix 1 + Matrix 2:")
    for row in result:
        print(row)

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