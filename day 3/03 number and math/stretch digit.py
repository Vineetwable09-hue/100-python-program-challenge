n = 4827

last_digit = n % 10
without_last = n // 10
tens_digit = without_last % 10
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output

check(last_digit, 7)
check(without_last, 482)
check(tens_digit, 2, hint="Remove the last digit first, then take the last digit of what remains.")
