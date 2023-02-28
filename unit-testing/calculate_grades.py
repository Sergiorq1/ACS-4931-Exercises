# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
# Refactored.
import math

def display_grade_stat():
    """Gathers stats and print them out."""
    grade_list = read_input()
    # Calculate the mean and standard deviation of the grades
    mean, standard_deviation = calculate_stat(grade_list)
    # print out the mean and standard deviation in a nice format.
    print_stat(mean, standard_deviation)

def read_input():
    """Get the inputs from the user."""
    grade_list = []
    n_student = 5
    for _ in range(0, n_student):
        grade_list.append(int(input('Enter a number: ')))
    return grade_list

def calculate_stat(grade_list):
    """Calculate the mean and standard deviation of the grades."""
    total = 0
    for grade in grade_list:
        total = total + grade
    mean = total / len(grade_list)
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grade_list)) # standard deviation
    return mean, sd

def print_stat(mean, sd):
    """print out the mean and standard deviation in a nice format."""
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')

# display_grade_stat()

def test_mean_standard_deviation_normal_use_case():
    grade_list = [2,3,3,4,4]
    actual_mean, actual_sd = calculate_stat(grade_list)
    
    expected_mean = 3.2
    expected_sd = 0.748

    assert math.isclose(actual_mean, expected_mean, rel_tol=0.1)
    assert math.isclose(actual_sd, expected_sd, rel_tol=0.1)