import json
import statistics
import sys

WEIGHTS = {
    'exam': 0.4,
    'midterm': 0.3,
    'homework': 0.3 # 5 assignments, each 6%
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

def main():
    data = read_grades(grade_file)
    final_grades = []
    print('Final Grades:')
    for student in data:
        grade = calculate_final_grade(student)
        final_grades.append(grade)
        print(f"{student['name']}: {grade:.2f}")
    print('\nClass Statistics:')
    print(f"Mean: {statistics.mean(final_grades):.2f}")
    print(f"Median: {statistics.median(final_grades):.2f}")
    print(f"Min: {min(final_grades):.2f}")
    print(f"Max: {max(final_grades):.2f}")
    print(f"Std Dev: {statistics.stdev(final_grades):.2f}" if len(final_grades) > 1 else "Std Dev: N/A")


    # TODO: efficiently sort the students based on final grades

if __name__ == '__main__':
    main()
