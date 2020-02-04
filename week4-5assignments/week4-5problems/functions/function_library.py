course_list = {}

def course_info():
    """Get a user's course information from an input prompt"""

    course_id_input = input("Please enter your course information with no spaces: ")

    course_is_ok= False

    while not course_is_ok:
        course_is_ok = validate_course_part(course_id_input)

        if not course_is_ok:
            course_id_input = input("Course ID is not valid. Please try again: ")
            course_is_ok = validate_course_part(course_id_input)
        else:
            course_list["Course ID"] = course_id_input 

    return course_id_input

def semester_info():
    """Get a user's course semester information from an input prompt"""

    semester_id_input = input("Please enter your course semester with no spaces: ")

    semester_is_ok= False

    while not semester_is_ok:
        semester_is_ok = validate_course_part(semester_id_input)

        if not semester_is_ok:
            semester_id_input = input("Course Semester is not valid. Please try again: ")
            semester_is_ok = validate_course_part(semester_id_input)
        else:
            course_list["Semester"] = semester_id_input 

    return semester_id_input

def validate_course_part(passed_course_part):
    """Validates course ID input is valid"""

    passed_course_part = passed_course_part.strip()

    if passed_course_part:
        if passed_course_part.isalnum():
            return True
        else:
            return False
    else:
        return False