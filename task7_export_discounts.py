# Task 7: Mini Project - Export Discounted Prices

prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000,
}

discount_input = input("Enter discount percentage: ").strip()

# Accept whole numbers or decimals (e.g. 10 or 12.5)
if not discount_input.replace(".", "", 1).isdigit():
    print("Invalid discount. Please enter a number.")
else:
    discount = float(discount_input)
    if discount > 100:
        print("Discount cannot be more than 100%.")
    else:
        total_discounted = 0

        # Write the report
        with open("discount_report.txt", "w") as file:
            file.write("Product | Original Price | Discounted Price\n")
            for product, price in prices.items():
                discounted_price = price - (price * discount / 100)
                total_discounted += discounted_price
                file.write(product + " | " + str(price) + " | " + str(round(discounted_price, 2)) + "\n")

            # Extra: summary at the bottom
            file.write("\nTotal Items: " + str(len(prices)) + "\n")
            file.write("Average Discounted Price: " + str(round(total_discounted / len(prices), 2)) + "\n")

        # Read the file back and print it
        with open("discount_report.txt", "r") as file:
            print(file.read())
