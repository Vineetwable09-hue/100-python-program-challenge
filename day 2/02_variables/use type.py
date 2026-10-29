sweets = 17
children = 5

each = 6//2
left_over = 5%3
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output

check(each, 3)
check(left_over, 2)
