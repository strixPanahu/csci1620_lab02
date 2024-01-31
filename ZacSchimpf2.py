"""
    Zac Schimpf
    CSCI 1620 001/851
    Professor Owora
    Week 02 - Lab 02
    29/01/2024
"""


def main():
    """
    Main logic structure that accepts students & scores, creates grade scale, and prints results
    :return: None
    """

    students = get_students()
    scores_list = get_scores(students)

    iteration = 1
    for current_score in scores_list:
        print("Student " + str(iteration) + " score is " + str(current_score[0]) + " and grade is " + current_score[1])
        iteration += 1


def get_students():
    """
    Requests input of quantity of students
    :return: int value of students
    """

    students = input("Total number of students: ").strip()
    try:
        students = int(students)

        if students < 0:
            raise IndexError

    except IndexError:
        print("\"" + str(students) + "\" must be a positive integer value.")
        students = get_students()

    except ValueError:
        print("\"" + str(students) + "\" must be a whole-number integer value, please try again.")
        students = get_students()

    return students


def get_scores(students):
    """
    Requests input of score and appends letter grade scale
    :param students: int quantity of students
    :return: 3-dimensional List[] containing score & letter grade; e.g. [[100, A], [0, F]]
    """

    try:
        scores = scores_input(students)
        scores = convert_to_list(students, scores)
        scores = append_letter_grades(scores)

    except ValueError:
        print("Scores must only include whole-number integer values between 0-100.")
        scores = get_scores(students)

    except IndexError:
        print("Scores contains the incorrect amount space-separated values for each student. "
              + "Please provide a minimum of " + str(students) + " values.")
        scores = get_scores(students)

    return scores


def scores_input(students):
    """
    Accepts user input, cleans, and validates spacing
    :param students: int value of students
    :return: String value user input; e.g. "100 70 50"
    """

    scores = input("Enter " + str(students) + " score(s): ").strip()

    spaces_count = scores.count(' ')
    score_breaks = students - 1
    if spaces_count < score_breaks:
        raise IndexError
    else:
        return scores


def convert_to_list(students, scores_str):
    """
    Processes conversion of values and creates grade scale
    :param scores_str: Space-separated integers within a String; e.g. "100 70 50"
    :param students: int quantity of students
    :return: 3-dimensional List[] containing only a score; e.g. [[100], [0]]
    """

    iterations = 0
    scores_substr = scores_str
    scores_list = []

    end_index = scores_substr.find(" ")
    if end_index == -1:
        current_score = int(scores_substr)
        scores_list.append([current_score])

        if current_score > 100 or current_score < 0:
            raise ValueError
    else:
        while iterations < students:
            end_index = scores_substr.find(" ")
            if end_index == -1:  # take whole value, if no spaces left
                current_score = int(scores_substr)
                scores_list.append([current_score])

                final_value = students - 1  # check for too few values
                if iterations != final_value:
                    raise IndexError
            else:
                current_score = int(scores_substr[:end_index])
                scores_list.append([current_score])

            if current_score > 100 or current_score < 0:
                raise ValueError

            end_index += 1  # shift value to skip current space char
            scores_substr = scores_substr[end_index:].strip()  # shift substring & clear duplicate spaces

            iterations += 1

    return scores_list


def append_letter_grades(scores):
    """
    Create weighted grade scale & append to provided scores
    :param scores: 3-dimensional List[] containing only a score; e.g. [[100], [0]]
    :return: 3-dimensional List[] containing score & letter grade; e.g. [[100, A], [0, F]]
    """

    best_score = max(scores)[0]
    d_cutoff = best_score - 40
    c_cutoff = best_score - 30
    b_cutoff = best_score - 20
    a_cutoff = best_score - 10

    iterations = 0
    for current_student in scores:
        if current_student[0] < d_cutoff:
            scores[iterations].append('F')
        elif current_student[0] < c_cutoff:
            scores[iterations].append('D')
        elif current_student[0] < b_cutoff:
            scores[iterations].append('C')
        elif current_student[0] < a_cutoff:
            scores[iterations].append('B')
        else:
            scores[iterations].append('A')
        iterations += 1

    return scores


main()
