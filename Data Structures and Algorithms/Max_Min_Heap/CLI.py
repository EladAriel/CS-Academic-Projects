# -*- coding: utf-8 -*-
"""
This script is an implementation of a Max-Min Heap program.
It allows users to build and manipulate a Max-Min Heap through a command line interface (CLI) menu. 

Libraries Used:
- max_min_heap: A class for implementing the Max-Min Heap data structure
- tkinter: A Python library used for creating GUIs
- textwrap: A module used for formatting text

Classes:
- Runner: A class used to run the CLI menu and implement the various heap operations
    - not_empty_heap(): A method that checks if the heap is not empty
    - open_menu(): A method that displays the welcome message and prompts the user to choose an option to build the heap or exit
    - second_menu(): A method that displays a menu with options to perform various heap operations, including printing the heap,
                     extracting the maximum or minimum node, inserting a new node, deleting a node, sorting the heap, or going back to the main menu
    - start_menu(): A method that starts the CLI menu and calls the open_menu() and second_menu() methods
    - getConnected(): A getter method that returns the value of the connected attribute

Functions:
- LoadHeapFile(): A function that prompts the user to select a text file, reads the file, and creates a list of numbers from its contents.
                  Special characters like '-' are allowed, but other non-numeric characters are ignored.
"""
# Import libraries
from max_min_heap import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import textwrap

class Runner:
    def __init__(self, heap):
        self.heap = Max_Min_Heap(heap)
        self.connected = True
        self.show_menu = True

    def not_empty_heap(self):
        """
        Checks if the heap is not empty.
        
        Returns:
            A boolean value indicating whether the heap is not empty.
        """
        return self.heap.__len__() > 0
    
    def open_menu(self):
        """
        Displays the welcome message and menu options to the user. 
        Validates user input and performs the chosen action.
        """        
        # Display the welcome message
        welcome_message = """
        Welcome to the Max-Min Heap program!
    
        This program allows you to build and manipulate a Max-Min Heap through a menu of options.
    
        Please choose one of the following options:
        [1] Build Heap
        [2] Exit
        """
        print(textwrap.dedent(welcome_message).strip())
        # Get the user's choice
        choice = input("> ")
        if self.not_empty_heap():
            # Validate the user's input
            if choice.isdigit() and int(choice) in [1, 2]:
                # The user input is valid
                if choice == "1":
                    # User chose to build a heap
                    self.heap.build_max_min_heap()
                    print("Heap built successfully.\n")
                elif choice == "2":
                    # User chose to exit
                    print("Exiting program...\n")
                    # Set show_menu to False to exit the GUI
                    self.show_menu = False
                    self.connected = False
            else:
                # The user input is invalid
                print("Invalid input. Please enter a valid choice (1 or 2).")
        else:
            manual_insert = input("You have uploaded an empty heap. Do you wish to insert the nodes manually? [Y/N]\n >")
            if manual_insert == "Y":
                print("Select [4] to insert a new node.\n")
                self.second_menu()
            else:
                print("Please exit the program and upload a non-empty heap.")

    def second_menu(self):
        """
         Displays a menu of options for manipulating the max-min heap and performs the selected operation.
        """
        # Display the menu of options
        second_menu_message = """
        Select an operation to perform:
        [1] Print the heap
        [2] Extract maximum node
        [3] Extract minimum node
        [4] Insert a new node
        [5] Delete a node
        [6] Sort the heap
        [7] Go back to main menu
        """
        print(textwrap.dedent(second_menu_message).strip())
        # Get the user's choice
        choice = input("> ")
        # Validate the user's input
        if choice.isdigit() and int(choice) in list(range(1,8)):
            # The user input is valid
            if choice == "1":
                # User chose to print the heap
                print(f"The max-min heap is:\n{self.heap.heap}\n")
            elif choice == "2":
                # User chose to extract the maximum node
                max_node = self.heap.heap_extract_max()
                new_heap = self.heap.heap
                print(f"The maximum node is: {max_node}\nThe new max-min heap is:\n{new_heap}\n")
            elif choice == "3":
                # User chose to extract the minimum node
                min_node = self.heap.heap_extract_min()
                new_heap = self.heap.heap
                print(f"The minimum node is: {min_node}\nThe new max-min heap is:\n{new_heap}\n")
            elif choice == "4":
                # User chose to insert a new node
                key = input("Enter the value of the node to be inserted: ")
                try:
                    key = float(key) if '.' in key else int(key)
                    self.heap.heap_insert(key)
                    new_heap = self.heap.heap
                    print(f"The inserted node is: {key}\nThe new max-min heap is:\n{new_heap}\n")
                except ValueError:
                    print("Invalid input. Please enter an valid value.")
            elif choice == "5":
                # Print the heap indexes on screen
                idx_list = list(range(self.heap.__len__() - 1))
                new_heap = self.heap.heap
                # User chose to delete a node
                deleted_node = input("Please enter the value of the node you want to delete.\n >")
                try:
                    if '.' in deleted_node:
                        idx = self.heap.heap.index(float(deleted_node))
                    else:
                        idx = self.heap.heap.index(int(deleted_node))
                    self.heap.heap_delete(idx)
                    print(f"The deleted node is: {deleted_node}\nThe new max-min heap is:\n{new_heap}\n")
                except ValueError:
                    print("Invalid input. Please enter an integer value.")                
            elif choice == "6":
                # Save the current heap
                current_heap = self.heap.heap[:]
                # User chose to sort the heap
                self.heap.heap_sort()
                print(f"The sorted heap is:\n{self.heap.heap}")
                restore_heap = input("Do you wish to restore the heap? [Y/N]\n> ")
                if restore_heap == "Y":
                    self.heap.heap = current_heap
            elif choice == "7":
                # User chose to go back to the main menu
                self.open_menu()
        else:
            # The user input is invalid
            print("Invalid input. Please enter a valid choice (1-7).")

    def start_menu(self):
        """
        Starts command line interface menu.
        """
        while self.show_menu:
            # Start open menu
            self.open_menu()
            # Check if heap is not empty
            while self.not_empty_heap() and self.show_menu:
                # Start second menu for heap operations
                self.second_menu() # Allows user to perform operations on heap

    def getConnected(self):
        """
        Get the current connection status of the CLI.
        
        Returns:
            bool: True if the CLI is connected to the backend, False otherwise.
        """
        return self.connected

def LoadHeapFile():
    """
    Prompts the user to select a text file, reads the file, and creates a list of numbers from its contents.
    Special characters like '-' are allowed, but other non-numeric characters are ignored.

    Returns:
        A list of numbers read from the selected file.
    """
    # Open a file dialog window and prompt the user to select a text file
    Tk().withdraw()
    file_path = askopenfilename(filetypes=[("Text Files", "*.txt")])
    try:
        with open(file_path, "r") as file:
            print("File opened successfully.\n")
            contents = file.read()
            try:
                heap = eval(contents)  # try to convert the file contents to a list
            except:
                heap = StrToList(contents)  # make a list of numbers out of the file
    except FileNotFoundError:  # error opening file
        print("Error: Couldn't open file %s." % file_path)
    except Exception as e:  # other errors
        print("Error: %s" % str(e))
    return heap

def StrToList(string):
    """
    Converts a string to a list of numbers. Special characters like '-' are allowed, but other non-numeric
    characters are ignored.

    Args:
        string: A string to be converted to a list of numbers.

    Returns:
        A list of numbers extracted from the input string.
    """
    # Check if the string is already a list
    try:
        num_list = eval(string)
    except:
        # Split the input string into a list of strings
        str_list = string.split()
        # Convert each string in the list to a number based on its format
        num_list = []
        for s in str_list:
            if all(c.isdigit() or c in ('.', '-') for c in s):
                if '.' in s:
                    try:
                        # Try to convert the string to a float
                        n = float(s)
                    except ValueError:
                        # If the string cannot be converted to a float, raise an exception
                        raise ValueError(f"Could not convert string '{s}' to a number")
                else:
                    try:
                        # Try to convert the string to an integer
                        n = int(s)
                    except ValueError:
                        # If the string cannot be converted to an integer, raise an exception
                        raise ValueError(f"Could not convert string '{s}' to a number")
                num_list.append(n)
    return num_list
