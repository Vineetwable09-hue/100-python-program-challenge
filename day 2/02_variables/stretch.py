import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
price = 10
quantity = 3
total = price * quantity
price = 20
quantity = quantity + 1

total_after = 30
new_total = 80
check(total_after, 30, hint="total was calculated once, on line 3.")
check(new_total, 80, hint="Re-do the multiplication with the current price and quantity.")
