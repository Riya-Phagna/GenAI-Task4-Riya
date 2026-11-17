# Task 2: Read File in Different Ways
# (run task1_write_sales.py first so sales_data.txt exists)
import os

if not os.path.exists("sales_data.txt"):
    print("sales_data.txt not found. Run task1_write_sales.py first.")
else:
    # 1. Read the entire file with read()
    with open("sales_data.txt", "r") as file:
        content = file.read()
    print("Using read():")
    print(content)

    # 2. Read only the first line with readline()
    with open("sales_data.txt", "r") as file:
        first_line = file.readline()
    print("Using readline():", first_line.strip())

    # 3. Read all lines with readlines() and convert to integers
    with open("sales_data.txt", "r") as file:
        lines = file.readlines()
    numbers = []
    for line in lines:
        line = line.strip()          # remove newline characters
        if line != "":               # skip blank lines
            numbers.append(int(line))
    print("Using readlines() as integers:", numbers)
