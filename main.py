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