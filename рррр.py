grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johny','Bilbo','Steve','Khendrik','Aaron'}

list_students = list(students)
list_students = sorted(list_students)

i = 0

for number in grades:
    grades[i] = sum(grades[i]) / len(grades[i])
    i = i+1

diary = dict(zip(list_students, grades))

print(diary)