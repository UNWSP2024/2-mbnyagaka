def calculate_total_purchase():
    # A customer in a store is purchasing five items.  
    # Write a program that asks for each item, 
    # then displays the subtotal of the sale, 
    # the amount of sales tax, and the total.  
    # Assume the sales tax is 7 percent.
    sales_tax_rate = 0.07
    subtotal = 0.0
    print("Enter the price of each of the five items.")
    for i in range(5):
        price_input = float(input(f"Enter price for item {i + 1}: "))
        subtotal += price_input
    sales_tax = subtotal * sales_tax_rate
    total_purchase = subtotal + sales_tax
    print(f"\nSubtotal: ${subtotal:.2f}")
    print(f"Sales tax rate: ${sales_tax:.2f}")
    print(f"Total purchase: ${total_purchase:.2f}")


calculate_total_purchase()