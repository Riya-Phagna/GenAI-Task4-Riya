# Task 3: Append New Sales
# (run task1_write_sales.py first so sales_data.txt exists)
import os

if not os.path.exists("sales_data.txt"):
    print("sales_data.txt not found. Run task1_write_sales.py first.")
else:
    new_sales = [5000, 2500, 1700]

    # Append mode adds to the end without erasing the old data
    with open("sales_data.txt", "a") as file:
        for sale in new_sales:
            file.write(str(sale) + "\n")

    # Reopen and print the updated file
    with open("sales_data.txt", "r") as file:
        print("Updated sales_data.txt:")
        print(file.read())

    # Extra: total number of lines after appending
    with open("sales_data.txt", "r") as file:
        line_count = len(file.readlines())
    print("Total number of lines:", line_count)
