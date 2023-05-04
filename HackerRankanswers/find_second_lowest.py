if __name__ == '__main__':
    students = []
    for _ in range(int(input('Number of students > '))):
        name = input('Student name > ')
        score = float(input('Score > '))
        students.append([name, score])
    
        
    students_score = []
    for each_student in students:
        student_score = each_student[1]
        students_score.append(float(student_score))
        
    sorted_score = sorted(list(set(students_score)))
    second = sorted_score[1]
    
    names = []
    for each_student in students:
        if each_student[1] == second:
            
            names.append(each_student[0])
    
    for each in sorted(names):        
        print(each)