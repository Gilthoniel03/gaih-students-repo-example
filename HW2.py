student_list = []
grade_list = []
average_grade = []
info = {}

for i in range(5):
    fullname = str(input("Enter your fullname:"))
    midterm = int(input("Enter your midterm grade:"))
    final = int(input("Enter your final grade:"))
    homework = int(input("Enter your hw grade:"))

    average = int(midterm + final + homework)/3
    student_list.append(fullname)
    grade_list.append([midterm,final,homework])
    average_grade.append(int(average))

    zip_list =  zip(student_list,grade_list)
    info = dict(zip_list)

print("NAMES",student_list)
print("ALL GRADES",grade_list)
print("GRADE WEIGH",average_grade)
print("INFORMATIONS",info)

average_grade.sort
print("SORTING OF THE GRADES",sorted(average_grade))
max(average_grade)
print("MAX GRADE",max(average_grade))
max_student = student_list[average_grade.index(max(average_grade))]
print("CONGRATS",max_student)




