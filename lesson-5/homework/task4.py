universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(universities):
    """
    Extract student enrollment and tuition fees from a list of universities.
    
    Parameters:
        universities (list): A list of lists containing university data.
    
    Returns:
        tuple: Two lists, one with student enrollments and one with tuition fees.
    """
    enrollments = [university[1] for university in universities]
    tuitions = [university[2] for university in universities]
    return enrollments, tuitions

def mean(data):
    """
    Calculate the mean of a list of numbers.
    
    Parameters:
        data (list): A list of numbers.
    
    Returns:
        float: The mean of the list.
    """
    return sum(data) / len(data)

def median(data):
    """
    Calculate the median of a list of numbers.
    
    Parameters:
        data (list): A list of numbers.
    
    Returns:
        float: The median of the list.
    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]

def main():
    # Get enrollment and tuition data
    enrollments, tuitions = enrollment_stats(universities)
    
    # Calculate totals
    total_students = sum(enrollments)
    total_tuition = sum(tuitions)
    
    # Calculate mean and median
    student_mean = mean(enrollments)
    student_median = median(enrollments)
    tuition_mean = mean(tuitions)
    tuition_median = median(tuitions)
    
    # Format and print the results
    print("******************************")
    print(f"Total students: {total_students:,}")
    print(f"Total tuition: $ {total_tuition:,}")
    print()
    print(f"Student mean: {student_mean:,.2f}")
    print(f"Student median: {student_median:,}")
    print()
    print(f"Tuition mean: $ {tuition_mean:,.2f}")
    print(f"Tuition median: $ {tuition_median:,}")
    print("******************************")

if __name__ == "__main__":
    main()