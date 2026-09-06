def gradingStudents(grades):
    result = []
    for grade in grades:
        if grades < 38: #if the students have marks below 38, just print the result
            result.append(grade)
        else:
            difference = 5 - (grade % 5) #if students have a mark near to a number multiple by 5, round up to that number
            if difference < 3: #but the number different should not be less than 3
                grade = grade + difference
                result.append(grade)
    return result 