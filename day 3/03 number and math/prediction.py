prediction = 4**2*3/8+2-1
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check(prediction, 7.0, hint="Do 4 ** 2 first, then * and /, left to right, then + and -. And remember that / gives a float.")
