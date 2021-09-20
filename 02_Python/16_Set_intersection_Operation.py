students_count_english = int(input())
student_english_set = set([int(x) for x in input().split()])
students_count_french = int(input())
student_french_set = set([int(x) for x in input().split()])

result = student_english_set.intersection(student_french_set)

print(len(result))
