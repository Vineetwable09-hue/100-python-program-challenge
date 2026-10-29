alphabet = "abcdefghijklmnopqrstuvwxyz"

every_other =alphabet[0::2]
last_five_reversed = alphabet[:-6:-1]
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output

check(every_other, "acegikmoqsuwy")
check(last_five_reversed, "zyxwv", hint="Start at the end with a negative step, and stop before the 6th-from-last letter: [:-6:-1].")
