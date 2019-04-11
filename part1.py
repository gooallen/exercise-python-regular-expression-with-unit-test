
"""

Byeongyun (Allen) Goo
goo00001@algonquinlive.com


Part 1:
Write a program that prints the numbers from 1 to 101.
But for multiples of three print "Smarty" instead of the number, and for multiples of five print "Pants".
For numbers which are multiples of both three and five, print "SmartyPants".

"""


import unittest

def check(i):
    # Check the number is multiples of both three and five
    # This line is first because it catches the specified numbers before below condition catches
    if i % 3 == 0 and i % 5 == 0:
        return "SmartyPants"
    # Check the number is multiples of three
    elif i % 3 == 0:
        return "Smarty"
    # Check the number is multiples of five
    elif i % 5 == 0:

        return "Pants"
    else:
        # print(i)
        return i


# Generate number from 1 to 101 by 'range(n, m)' and loop through 'for'
for i in range(1, 102):
    print(check(i))


# Testing with different expected values
class TestPart1(unittest.TestCase):
    # Expect both expected and actual number
    def test_num_2(self):
        self.assertEqual(check(2), 2)

    # Expect string "Smarty" as the number is multiples of three
    def test_num_3(self):
        self.assertEqual(check(3), "Smarty")

    # Expect string "Pants" as the number is multiples of five
    def test_num_10(self):
        self.assertEqual(check(10), "Pants")

    # Expect string "SmartyPants" as the number is multiples of both three and five
    def test_num_15(self):
        self.assertEqual(check(15), "SmartyPants")

    # Expect string "SmartyPants" as the number is multiples of both three and five
    def test_num_45(self):
        self.assertEqual(check(15), "SmartyPants")

    # Expect string "Smarty" as the number is multiples of three
    def test_num_99(self):
        self.assertEqual(check(99), "Smarty")

    # Expect same number for both expected and actual number
    def test_num_101(self):
        self.assertEqual(check(101), 101)

    if __name__ == '__main__':
        unittest.main()
