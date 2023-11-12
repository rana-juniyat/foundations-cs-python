#Global variable to store information about open tabs.
tabs = []
current_tab = None
# Function to add a new tab
def open_tab():
    title = input("Enter the title of the website: ")
    url = input("Enter the URL of the website: ")
    tab = {"title": title, "url": url, "nested_tabs": []}
    tabs.append(tab)
##############################
# Code for closing a tab
def close_tab():
    global current_tab
    if tabs:
        index = int(input("Enter the index of the tab to close (default is the last tab): ") or -1)
        if 0 <= index < len(tabs):
            closed_tab = tabs.pop(index)
            if current_tab == closed_tab:
                current_tab = tabs[-1] if tabs else None
            print(f"Closed tab: {closed_tab['title']}")
        else:
            print("Invalid tab index.")
    else:
        print("No tabs to close.")

##############################
import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.geeksforgeeks.org/")
soup = BeautifulSoup(req.content, "html.parser")
print(soup.prettify())
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
            close_tab(index=None)
        elif choice == "3":
            switch_tab(index=None)
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
