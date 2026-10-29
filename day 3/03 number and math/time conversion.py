total_seconds = 98765

hours = 98765//3600
minutes = ( 98765%3600)//60
seconds = 98765%60

import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check(hours, 27)
check(minutes, 26)
check(seconds, 5)
