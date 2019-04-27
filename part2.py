
"""
Byeongyun (Allen) Goo
hello@allengoo.com


Part 2:
Write a program that accepts a list of numbers (real or integer),
and then calculates and displays the median, the average and the sum of the numbers.

Then the program should generate and display a new list containing the numbers in descending sorted order.

Finally, the program should generate and display two new lists:
- the first displays the numbers that have digits "1" and "5" in it
- the second displays the numbers that have digits "1" or "5" in it

"""

import statistics
import re
import unittest


# Create a new list for the digits_and() function
list_temp1 = []
# Create a new empty string to hold value during for loop for the digits_and() function
string_temp1 = ''
# Create a new list for the digits_or() function
list_temp2 = []
# Create a new empty string to hold value during for loop for the digits_or() function
string_temp2 = ''
# Create an empty list for split string from user input
split_string_list = []



# Function calculating the average from the list
def average_list(list):
    return sum(list) / len(list)

# Function calculating the median from the list
def median_list(list):
    return statistics.median(list)

# Function calculating sum from the list
def sum_list(list):
    return sum(list)

# Function sorting in descending order from the list
def sort_reverse(list):
    sorted_list_des = list
    sorted_list_des.sort(reverse=True)
    return sorted_list_des

# Function sorting the number contains '1' and '5' from the (string) list
def digits_and(list):
    for item in list:
        # Searching '1' and '5' in the number(s)
        search = re.search(r'^(?=.*[1])(?=.*[5])', item)
        string_temp1 = item
        if search:
            # Converted to float considering consistency and append to list_temp1 to display
            list_temp1.append(float(string_temp1))
    return list_temp1

# Function sorting the number contains '1' or '5' from the (string) list
def digits_or(list):
    for item in list:
        # Searching '1' or '5' in the number(s)
        search = re.search(r'([1]|[5])', item)
        string_temp2 = item
        if search:
            # Converted to float considering consistency and append to list_temp2 to display
            list_temp2.append(float(string_temp2))
    return list_temp2


# User input
input_number = input("Enter list of number(s) separated by comma (ex. 1,2,3): ")
# Split each value from user input and insert to new list called split_string_list
split_string_list = input_number.split(",")

# Convert string to float which makes easier to calculate for next steps
float_list = [float(x) for x in split_string_list]
print("The list of the number(s): ", float_list)
print("The median of the number(s):", median_list(float_list))
print("The average of the number(s):", average_list(float_list))
print("The sum of the number(s):", sum_list(float_list))
print("The list of the number(s) in descending sorted order:", sort_reverse(float_list))
print("The list of the number(s) that have digits '1' and '5' in it:", digits_and(split_string_list))
print("The list of the number(s) that have digits '1' or '5' in it:", digits_or(split_string_list))



# Reset all instances for the test
list_temp1 = []
string_temp1 = ''
list_temp2 = []
string_temp2 = ''
split_string_list = []

# Testing each function
class TestPart2(unittest.TestCase):

    # Expect the average value from the list
    def test_average_list(self):
        self.assertEqual(average_list([50, 62.2, 30, 25]), 41.8)

    # Expect the median value from the list
    def test_median_list(self):
        self.assertEqual(median_list([100, 34, 25, 30, 25]), 30)

    # Expect the sum value from the list
    def test_sum_list(self):
        self.assertEqual(sum_list([95, 2, 31, 87, 22.2]), 237.2)

    # Expect sorting in descending order from the list
    def test_sort_reverse(self):
        self.assertEqual(sort_reverse([4, 2, 52.1, 87, 67.9]), [87, 67.9, 52.1, 4, 2])

    # Expect sorting the number contains '1' and '5' from the (string) list
    def test_digits_and(self):
        self.assertEqual(digits_and(['1', '2', '3', '4', '15', '51']), [15, 51])

    # Expect sorting the number contains '1' or '5' from the (string) list
    def test_digits_or(self):
        self.assertEqual(digits_or(['1', '2']), [1])

    if __name__ == '__main__':
        unittest.main()


