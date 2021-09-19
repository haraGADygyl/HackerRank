students_count_english = int(input())
students_english = set([int(x) for x in input().split()])
students_count_french = int(input())
students_french = set([int(x) for x in input().split()])

result = students_english.union(students_french)

print(len(result))
