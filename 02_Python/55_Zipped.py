grades_count, students_count = [int(x) for x in input().split()]

grades_list = []

for _ in range(students_count):
    grades = [float(x) for x in input().split()]
    grades_list.append(grades)

for i in list(zip(*grades_list)):
    print(sum(i) / students_count)
