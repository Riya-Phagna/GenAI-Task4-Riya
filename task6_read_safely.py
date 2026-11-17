# Task 6: Read File Safely
import os

filename = input("Enter the filename to open: ").strip()

if os.path.exists(filename):
    with open(filename, "r") as file:
        print(file.read())
else:
    print("File not found. Please check the filename.")
