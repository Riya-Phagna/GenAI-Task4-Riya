# Task 1: Write Sales Records to a File

sales = [1200, 450, 980, 1500, 3000]

# Open in write mode and write each sale on a new line
with open("sales_data.txt", "w") as file:
    for sale in sales:
        file.write(str(sale) + "\n")

# Reopen and print the contents
with open("sales_data.txt", "r") as file:
    print("Contents of sales_data.txt:")
    print(file.read())

# Extra: comma-separated format (saved in a separate file so sales_data.txt stays unchanged)
with open("sales_data_comma.txt", "w") as file:
    file.write(",".join(str(sale) for sale in sales))

with open("sales_data_comma.txt", "r") as file:
    print("Comma-separated version:", file.read())
