# Task 5: Create Product Info File (User Input)

# 1 & 2. Ask for 3 products and write them as: ProductName | Price
with open("products.txt", "w") as file:
    for i in range(3):
        name = input("Enter product name " + str(i + 1) + ": ").strip()
        price = input("Enter price for " + name + ": ").strip()
        file.write(name + " | " + price + "\n")

# 4. Read the file and print each line
print("\nProducts in file:")
with open("products.txt", "r") as file:
    for line in file:
        print(line.strip())
