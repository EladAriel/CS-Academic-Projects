# -*- coding: utf-8 -*-
"""
This is the main program file for the heap manipulation program.
"""
# Import necessary libraries and modules
from CLI import *

# Load the heap from the heap file
heap = LoadHeapFile()

# Create a new instance of the Runner class
runner = Runner(heap)

# Run the program in a loop until the user decides to exit
while runner.getConnected():
    runner.start_menu()

# Exit the program when the loop is done
print("Thank you for using the heap manipulation program.")