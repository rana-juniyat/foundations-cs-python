# Import necessary libraries
import os
import json
import requests
from bs4 import BeautifulSoup
# Global variables
tabs = []
current_tab = None
##########################################################################################################
#if choice == "1":
##################
# Function to add a new tab
def open_tab():
    """
    Opens a new tab and sets it as the current tab.
    """
    global tabs, current_tab  

    title = input("Enter the title of the website: ")
    url = input("Enter the URL of the website: ")

    # Basic input validation
    if not title or not url:
        print("Error: Title and URL cannot be empty.")
        return

    tab = {"title": title, "url": url, "nested_tabs": []}
    tabs.append(tab)
    current_tab = tab  # Set the current tab to the newly opened tab
    print(f"Tab '{title}' opened successfully.")
    
#Time Complexity: O(1)
#Justification: Constant time complexity; the function performs a fixed number of operations regardless of input size.

##########################################################################################################
#elif choice == "2":
####################
# Function to close a tab
def close_tab(index=None):
    """
    Chooses the specified tab or the last opened tab if no index is provided.
    """
    global tabs, current_tab  # Indicate that 'tabs' and 'current_tab' are global variables

    if index is None:
        # If no index is provided, close the last opened tab
        if tabs:
            closed_tab = tabs.pop()
            if current_tab == closed_tab:
                current_tab = tabs[-1] if tabs else None
            print(f"Tab '{closed_tab['title']}' closed successfully.")
        else:
            print("No tabs to close.")
    elif 0 <= index < len(tabs):
        # Close the tab at the specified index
        closed_tab = tabs.pop(index)
        if current_tab == closed_tab:
            current_tab = tabs[-1] if tabs else None
        print(f"Tab '{closed_tab['title']}' closed successfully.")
    else:
        print("Invalid tab index.")

##########################################################################################################
#elif choice == "3":
####################
# Assuming we have the 'requests' and 'beautifulsoup4' libraries installed:
# I installed them using: pip install requests beautifulsoup4

# Function to display the HTML content of a tab's URL
def switch_tab(index=None):
    """
    Display the HTML content of the specified tab or the last opened tab if no index is provided.
    """
    global current_tab  # Indicate that 'current_tab' is a global variable

    if index is None:
        tab = current_tab
    elif 0 <= index < len(tabs):
        tab = tabs[index]
    else:
        print("Invalid tab index.")
        return

    url = tab.get("url")
    if url:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Check if the request was successful
            html_content = response.text

            # Use BeautifulSoup to parse and print the HTML content
            soup = BeautifulSoup(html_content, 'html.parser')
            print("HTML Content of", tab["title"])
            print("=========================")
            print(soup.prettify())
        except requests.RequestException as e:
            print(f"Error fetching content: {e}")
    else:
        print("Tab has no associated URL.")
##########################################################################################################
#elif choice == "4":
####################
# Function to display the titles of all open tabs hierarchically
def display_all_tabs():
    """
    Display the titles of all open tabs hierarchically.
    """
    global tabs  # Indicate that 'tabs' is a global variable

    if not tabs:
        print("No tabs to display.")
        return

    print("Open Tabs:")
    for i, tab in enumerate(tabs):
        display_tab(tab, depth=0)

# Helper function to display a tab and its nested tabs recursively
def display_tab(tab, depth):
    indentation = "  " * depth
    print(f"{indentation}- {tab['title']}")

    # Display nested tabs recursively
    for nested_tab in tab['nested_tabs']:
        display_tab(nested_tab, depth + 1)
##########################################################################################################
#elif choice == "5":
####################
# Function to create nested tabs
def open_nested_tab():
    """
    Creats nested tabs under a specified parent tab.
    """
    global tabs 

    if not tabs:
        print("No open tabs to nest under.")
        return

    index = input("Enter the index of the parent tab where you want to insert nested tabs: ")
    if not index.isdigit():
        print("Invalid index. Please enter a valid number.")
        return

    index = int(index)
    if 0 <= index < len(tabs):
        parent_tab = tabs[index]
        nested_tab_count = int(input("Enter the number of nested tabs you want to create: "))

        for _ in range(nested_tab_count):
            title = input("Enter the title of the nested tab: ")
            content = input("Enter the content of the nested tab: ")

            nested_tab = {"title": title, "content": content, "nested_tabs": []}
            parent_tab['nested_tabs'].append(nested_tab)

        print(f"{nested_tab_count} nested tabs created under '{parent_tab['title']}'.")
    else:
        print("Invalid parent tab index.")
##########################################################################################################
#elif choice == "6":
####################
# Function to clear all opened tabs
def clear_all_tabs():
    """
    Clears all opened tabs.
    """
    global tabs, current_tab 

    if not tabs:
        print("No tabs to clear.")
        return

    tabs = []  # Clear the list of open tabs
    current_tab = None  # Reset the current tab
    print("All opened tabs cleared.")
##########################################################################################################
#elif choice == "7":
####################
# Function to save tabs to a file
def save_tabs():
    """
    Saves the current state of open tabs to a file in JSON format.
    """
    global tabs  

    file_path = input("Enter the file path to load tabs from (e.g., C:/path/to/tabs.json): ")

    with open(file_path, 'w') as file:
        json.dump(tabs, file, indent=2)

    print("Tabs saved successfully.")
##########################################################################################################
#elif choice == "8":
####################
# Function to load tabs from a specified file path
def import_tabs(file_path):
    """
    Loads tabs from a specified file path.
    """
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            try:
                tabs_data = json.load(file)
                # Process tabs_data as needed
                print("Tabs loaded successfully.")
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON from file: {e}")
    else:
        print(f"File not found: {file_path}")

##########################################################################################################
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
    # Print current working directory
    print("Current Working Directory:", os.getcwd())

    while True:
        menu()
        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            open_tab()

        elif choice == "2":
            index = input("Enter the index of the tab to close (default is the last opened tab): ")
            close_tab(int(index) if index.isdigit() else None)

        elif choice == "3":
            index = input("Enter the index of the tab to display content (default is the last opened tab): ")
            switch_tab(int(index) if index.isdigit() else None)
        elif choice == "4":
            display_all_tabs()
        elif choice == "5":
            open_nested_tab()
        elif choice == "6":
            clear_all_tabs()
        elif choice == "7":
            save_tabs()
        elif choice == "8":
            file_path = input("Enter the file path to load tabs from (e.g., tabs.json): ")
            import_tabs(file_path)
        elif choice == "9":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
