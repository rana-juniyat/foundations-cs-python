#Global variable to store information about open tabs.
tabs = []
# Function to add a new tab
def open_tab():
    title = input("Enter the title of the website: ")
    url = input("Enter the URL of the website: ")
    tab = {"title": title, "url": url, "nested_tabs": []}
    tabs.append(tab)
##############################
def close_tab(index=None):
    if index is None:
        tabs.pop()
    else:
        tabs.pop(index)
##########################
#       Main & Menu
##########################
# Function to display the menu options
def menu():
    print("\nWelcome to the Advanced Browser Tabs Simulation!")
    print("1. Open Tab")
    print("2. Close Tab")
    print("3. Switch Tab")
    print("4. Display All Tabs")
    print("5. Open Nested Tab")
    print("6. Clear All Tabs")
    print("7. Save Tabs")
    print("8. Import Tabs")
    print("9. Exit")

def main():
    while True:
        menu()
        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            open_tab()

        elif choice == "2":
            index = int(input("Enter the index of the tab to close: ") or -1)
            close_tab(index)
        elif choice == "3":
            switch_tab()
        elif choice == "4":
            display_all_tabs()
        elif choice == "5":
            open_nested_tab()
        elif choice == "6":
            clear_all_tabs()
        elif choice == "7":
            save_tabs()
        elif choice == "8":
            import_tabs()
        elif choice == "9":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
