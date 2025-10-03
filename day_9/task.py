student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for name in student_scores:
    Grade = ""
    if student_scores[name] >= 91 and student_scores[name] <= 100:
        Grade = "Outstanding"
        student_grades.update({name : Grade})
    elif student_scores[name] >= 81 and student_scores[name] <= 90:
        Grade = "Exceed Expectations"
        student_grades.update({name : Grade})
    elif student_scores[name] >= 71 and student_scores[name] <= 80:
        Grade = "Acceptable"
        student_grades.update({name : Grade})
    else:
        Grade = "Fail"
        student_grades.update({name : Grade})

print(student_grades)