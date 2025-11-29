from domain.Course import Course
from domain.Student import Student
from utils import get_padding

c = Course("Math", "Jhon")
a = Course("Romanian", "Ana")
print(c)
l =[c,a,c,a]
print(Course.courselist_as_table(l,"example"))
print(l)
s=Student("Ana")
s2=Student("George")
print(s)
l=[s,s2,s,s2]
print(Student.studentlist_as_table(l,"Example2"))
print(l)