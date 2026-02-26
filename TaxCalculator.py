def taxCalculation(x):
    sales_tax = x * .06
    total_and_tax = x + sales_tax
    print("Sales tax:\t", round(sales_tax, 2))
    print("Total after tax:", round(x, 2))