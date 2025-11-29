from domain.Course import Course
from utils import get_padding

c = Course("Math", "Jhon")
a = Course("Romanian", "Ana")
print(c)
l =[c,a,c,a]
print(Course.courselist_as_table(l,"example"))
print(l)