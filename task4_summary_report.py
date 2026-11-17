# Task 4: Generate Summary Report from File
# (run tasks 1 and 3 first so sales_data.txt has all the sales)
import os

if not os.path.exists("sales_data.txt"):
    print("sales_data.txt not found. Run task1_write_sales.py first.")
else:
    sales = []
    with open("sales_data.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line != "":
                sales.append(int(line))

    if len(sales) == 0:
        print("The file has no sales data.")
    else:
        print("Total Sales:", sum(sales))
        print("Highest Sale:", max(sales))
        print("Lowest Sale:", min(sales))
        print("Average Sale:", round(sum(sales) / len(sales), 2))
