import json
import statistics
import sys

WEIGHTS = {
    'exam': 0.4,
    'midterm': 0.3,
    'homework': 0.06 # 5 assignments, each 6%
}

grade_file = "grades.json"

def read_grades(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def calculate_final_grade(student):
    homework_grades = student['homework']
    homework_sum = sum(homework_grades)
    homework_score = homework_sum * WEIGHTS['homework'] 
    avg_homework = homework_sum / len(homework_grades)
    return (
        student['exam'] * WEIGHTS['exam'] + student['midterm'] * WEIGHTS['midterm'] + homework_score
    )

# Efficient algorithm to sort students by final grade
def sort_students(students):
    n = len(students)
    for i in range(n):
        for j in range(0, n-i-1):
            if students[j][1] < students[j+1][1]:
                students[j], students[j+1] = students[j+1], students[j]
    return students

def main():
    data = read_grades(grade_file)
    final_grades = []
    print('Final Grades:')
    for student in data:
        try:
            grade = calculate_final_grade(student)
            final_grades.append((student['name'], grade))
            # print(f"{student['name']}: {grade:.2f}")
        except Exception as e:
            pass
    sorted_students = sort_students(final_grades)
    for i, (student, grade) in enumerate(sorted_students, start=1):
        print(f"{i}. {student}: {grade:.2f}")
    print('\nClass Statistics:')
    print(f"Mean: {statistics.mean([grade for _, grade in final_grades]):.2f}")
    print(f"Median: {statistics.median([grade for _, grade in final_grades]):.2f}")
    print(f"Min: {min([grade for _, grade in final_grades]):.2f}")
    print(f"Max: {max([grade for _, grade in final_grades]):.2f}")
    print(f"Std Dev: {statistics.stdev([grade for _, grade in final_grades]):.2f}")

if __name__ == '__main__':
    main()