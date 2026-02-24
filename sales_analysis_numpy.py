"""
project: Sales Data Analysis using NumPy
Author: Jyoti Soni
Description:
This project analyzes yearly sales data of 5 products
using NumPy operations.
"""

import numpy as np


# ------------------------------
# 1. Generate Sales Data
# ------------------------------
def generate_sales_data():
    np.random.seed(10)
    sales = np.random.randint(1000,5000,(12,5))
    return sales

# ------------------------------
# 2. Monthly Total Sales
# ------------------------------
def monthly_total(sales):
    return sales.sum(axis=1)


# ------------------------------
# 3. Product Wise Total Sales
# ------------------------------
def product_total(sales):
    return sales.sum(axis=0)

# ------------------------------
# 4. Best Selling Product
# ------------------------------
def best_product(sales):
    totals = sales.sum(axis=0)
    index = np.argmax(totals)
    return index,totals[index]

# ------------------------------
# 5. Worst Performing Month
# ------------------------------
def worst_month(sales):
    totals = sales.sum(axis=1)
    index = np.argmin(totals)
    return index,totals[index]

# ------------------------------
# 6. Monthly Growth Percentage
# ------------------------------
def growth_rate(sales):
    monthly = sales.sum(axis=1)
    growth = np.diff(monthly)/monthly[:-1]*100
    return growth


# ------------------------------
# 7. Increase Sales by 10%
# ------------------------------
def increase_sales(sales):
    return sales*1.10

# ------------------------------
# 8. Filter High Revenue Months
# ------------------------------
def high_revenue_months(sales):
    monthly = sales.sum(axis=1)
    return monthly[monthly>15000]



# ------------------------------
# Main Execution
# ------------------------------
def main():
    sales = generate_sales_data()

    print("Sales Data:\n", sales)
    print("\nMonthly Total:\n", monthly_total(sales))
    print("\nProduct Total:\n", product_total(sales))
    
    best_idx, best_value = best_product(sales)    
    print(f"\nBest Product: Product {best_idx} with sales {best_value}")
    
    
    worst_idx, worst_value = worst_month(sales)    
    print(f"\nWorst Month: Month {worst_idx+1} with sales {worst_value}")
    
    print("\nGrowth Percentage:\n", growth_rate(sales))
    print("\nincrease sales: \n",increase_sales(sales))
    print("\nHigh Revenue Months:\n", high_revenue_months(sales))


if __name__ == "__main__":
    main()


























































