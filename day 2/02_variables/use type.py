import sys
sys.path.insert(0, "../src")
from course_tools import check, check_output
t1 = "int"
t2 = "float"
t3 = "str"
t4 = "bool"
t5 = "float"
check(t1, "int")
check(t2, "float")
check(t3, "str")
check(t4, "bool", hint="A comparison asks a yes/no question.")
check(t5, "float", hint="What happens when you mix an int and a float?")
