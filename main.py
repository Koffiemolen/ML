# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Make total sales column (doesn't work, adds as string)



# remove $ sign from price column
car_sales["Price"] = car_sales["Price"].str.replace('[\$\,\.]', '').astype(int)
car_sales["Total Sales"] = car_sales["Price"].astype(int).cumsum()
car_sales

# Plot the total sales
