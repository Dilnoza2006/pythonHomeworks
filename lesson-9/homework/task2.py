import csv

# Read data from grades.csv
def read_grades(file_path='grades.csv'):
    grades = []
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['Grade'] = int(row['Grade'])  # Convert grade to integer
            grades.append(row)
    return grades

# Calculate average grade for each subject
def calculate_average_grades(grades):
    subject_grades = {}
    for entry in grades:
        subject = entry['Subject']
        grade = entry['Grade']
        if subject not in subject_grades:
            subject_grades[subject] = []
        subject_grades[subject].append(grade)
    average_grades = {
        subject: sum(grades) / len(grades)
        for subject, grades in subject_grades.items()
    }
    return average_grades

# Write average grades to a new CSV file
def write_average_grades(average_grades, file_path='average_grades.csv'):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Subject', 'Average Grade'])
        for subject, avg_grade in average_grades.items():
            writer.writerow([subject, avg_grade])
    print(f'Average grades written to {file_path}')

if __name__ == '__main__':
    grades = read_grades()
    average_grades = calculate_average_grades(grades)
    write_average_grades(average_grades)
