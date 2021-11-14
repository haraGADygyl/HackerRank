# students_count = int(input())
# index = input().split().index('MARKS')
#
# total = 0
# for i in range(students_count):
#     data = input().split()
#
#     total += int(data[index])
#
# print(f'{total/students_count:.2f}')
#
from collections import namedtuple

students_count = int(input())

Student = namedtuple('Student', input().split())

total = 0
for _ in range(students_count):
    student = Student(*input().split())
    total += int(student.MARKS)

print(f'{total / students_count:.2f}')
